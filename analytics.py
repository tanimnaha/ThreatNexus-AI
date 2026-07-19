from utils.map_generator import load_threats
from utils.threat_analyzer import analyze_threats


def get_analytics():

    threats = load_threats()

    analysis = analyze_threats(threats)

    analytics = {

        "total_threats": len(threats),

        "critical": analysis["critical_count"],

        "high": analysis["high_count"],

        "medium": analysis["medium_count"],

        "low": analysis["low_count"],

        "threat_score": analysis["threat_score"],

        "risk_level": analysis["risk_level"],

        "recommendation": analysis["recommendation"],

        "top_country": analysis["top_country"],

        "top_attack": analysis["top_attack"],

    }

    return analytics