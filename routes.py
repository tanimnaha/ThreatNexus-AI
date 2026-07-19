from flask import (
    Blueprint,
    render_template,
    Response,
    send_file,
    request,
)

from utils.map_generator import create_world_map, load_threats
from utils.chart_generator import (
    create_severity_chart,
    create_timeline_chart,
)
from utils.country_chart import create_country_chart
from utils.attack_chart import create_attack_chart
from utils.status_chart import create_status_chart
from utils.auto_refresh import get_refresh_status
from utils.threat_analyzer import analyze_threats
from utils.analytics import get_analytics
from utils.report_generator import (
    generate_csv_report,
    generate_pdf_report,
)
from utils.virustotal_lookup import lookup_ip, lookup_domain


main = Blueprint("main", __name__)


@main.route("/")
def index():
    return render_template("index.html")


@main.route("/dashboard")
def dashboard():

    threats = load_threats()

    search = request.args.get("search", "").lower().strip()
    severity = request.args.get("severity", "").strip()

    # VirusTotal IOC Lookup
    ioc = request.args.get("ioc", "").strip()
    vt_result = None

    if ioc:
        try:
            if "." in ioc and not ioc.replace(".", "").isdigit():
                vt_result = lookup_domain(ioc)
            else:
                vt_result = lookup_ip(ioc)
        except Exception:
            vt_result = None

    filtered = []

    for threat in threats:

        if search:

            text = " ".join([
                str(threat.get("ip", "")),
                str(threat.get("country", "")),
                str(threat.get("city", "")),
                str(threat.get("type", "")),
            ]).lower()

            if search not in text:
                continue

        if severity:

            if threat.get("severity") != severity:
                continue

        filtered.append(threat)

    analysis = analyze_threats(filtered)

    total = len(filtered)

    critical = sum(
        1 for t in filtered
        if t["severity"] == "Critical"
    )

    high = sum(
        1 for t in filtered
        if t["severity"] == "High"
    )

    medium = sum(
        1 for t in filtered
        if t["severity"] == "Medium"
    )

    low = sum(
        1 for t in filtered
        if t["severity"] == "Low"
    )

    return render_template(
        "dashboard.html",

        threats=filtered,
        live_feed=filtered[:10],

        total_threats=total,
        critical=critical,
        high=high,
        medium=medium,
        low=low,

        world_map=create_world_map(),
        severity_chart=create_severity_chart(),
        timeline_chart=create_timeline_chart(),

        country_chart=create_country_chart(),
        attack_chart=create_attack_chart(),
        status_chart=create_status_chart(),

        refresh_status=get_refresh_status(),

        threat_score=analysis["threat_score"],
        risk_level=analysis["risk_level"],
        recommendation=analysis["recommendation"],
        top_country=analysis["top_country"],
        top_attack=analysis["top_attack"],

        # VirusTotal
        ioc=ioc,
        vt_result=vt_result,
    )


@main.route("/analytics")
def analytics():

    analytics = get_analytics()

    return render_template(
        "analytics.html",

        total_threats=analytics["total_threats"],
        critical=analytics["critical"],
        high=analytics["high"],
        medium=analytics["medium"],
        low=analytics["low"],

        threat_score=analytics["threat_score"],
        risk_level=analytics["risk_level"],
        recommendation=analytics["recommendation"],
        top_country=analytics["top_country"],
        top_attack=analytics["top_attack"],

        severity_chart=create_severity_chart(),
        timeline_chart=create_timeline_chart(),

        country_chart=create_country_chart(),
        attack_chart=create_attack_chart(),
        status_chart=create_status_chart(),
    )


@main.route("/reports")
def reports():

    analytics = get_analytics()

    return render_template(
        "reports.html",

        total_threats=analytics["total_threats"],
        critical=analytics["critical"],
        high=analytics["high"],
        medium=analytics["medium"],
        low=analytics["low"],

        threat_score=analytics["threat_score"],
        risk_level=analytics["risk_level"],
        recommendation=analytics["recommendation"],
        top_country=analytics["top_country"],
        top_attack=analytics["top_attack"],
    )


@main.route("/about")
def about():
    return render_template("about.html")


@main.route("/download/csv")
def download_csv():

    threats = load_threats()

    csv_buffer = generate_csv_report(threats)

    return Response(
        csv_buffer.getvalue(),
        mimetype="text/csv",
        headers={
            "Content-Disposition":
            "attachment; filename=ThreatNexus_AI_Report.csv"
        },
    )


@main.route("/download/pdf")
def download_pdf():

    threats = load_threats()

    analysis = analyze_threats(threats)

    pdf_buffer = generate_pdf_report(analysis)

    return send_file(
        pdf_buffer,
        as_attachment=True,
        download_name="ThreatNexus_AI_Report.pdf",
        mimetype="application/pdf",
    )