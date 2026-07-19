import requests
from datetime import datetime
from flask import current_app

BASE_URL = "https://www.virustotal.com/api/v3"


def _headers():
    return {
        "x-apikey": current_app.config["VIRUSTOTAL_API_KEY"]
    }


def _format_timestamp(timestamp):
    if not timestamp:
        return "N/A"

    try:
        return datetime.utcfromtimestamp(
            int(timestamp)
        ).strftime("%d %b %Y • %I:%M %p UTC")
    except Exception:
        return str(timestamp)


def lookup_ip(ip):

    url = f"{BASE_URL}/ip_addresses/{ip}"

    response = requests.get(url, headers=_headers())

    if response.status_code != 200:
        return None

    data = response.json()["data"]["attributes"]

    stats = data.get("last_analysis_stats", {})

    return {
        "type": "IP Address",
        "query": ip,
        "country": data.get("country", "Unknown"),
        "reputation": data.get("reputation", 0),
        "harmless": stats.get("harmless", 0),
        "malicious": stats.get("malicious", 0),
        "suspicious": stats.get("suspicious", 0),
        "undetected": stats.get("undetected", 0),
        "timeout": stats.get("timeout", 0),
        "last_analysis_date": _format_timestamp(
            data.get("last_analysis_date")
        ),
        "tags": data.get("tags", []),
        "asn": data.get("asn", "N/A"),
        "as_owner": data.get("as_owner", "N/A"),
        "network": data.get("network", "N/A"),
    }


def lookup_domain(domain):

    url = f"{BASE_URL}/domains/{domain}"

    response = requests.get(url, headers=_headers())

    if response.status_code != 200:
        return None

    data = response.json()["data"]["attributes"]

    stats = data.get("last_analysis_stats", {})

    return {
        "type": "Domain",
        "query": domain,
        "country": data.get("country", "Unknown"),
        "reputation": data.get("reputation", 0),
        "harmless": stats.get("harmless", 0),
        "malicious": stats.get("malicious", 0),
        "suspicious": stats.get("suspicious", 0),
        "undetected": stats.get("undetected", 0),
        "timeout": stats.get("timeout", 0),
        "last_analysis_date": _format_timestamp(
            data.get("last_analysis_date")
        ),
        "tags": data.get("tags", []),
        "asn": data.get("asn", "N/A"),
        "as_owner": data.get("as_owner", "N/A"),
        "network": data.get("network", "N/A"),
    }