from collections import Counter


def analyze_threats(threats):
    """
    Analyze threat data and return AI-generated insights.
    """

    if not threats:

        return {
            "threat_score": 0,
            "risk_level": "LOW",
            "recommendation": "No threat data available.",
            "top_country": "N/A",
            "top_attack": "N/A",
            "critical_count": 0,
            "high_count": 0,
            "medium_count": 0,
            "low_count": 0,
        }

    critical = sum(
        1 for threat in threats
        if threat.get("severity") == "Critical"
    )

    high = sum(
        1 for threat in threats
        if threat.get("severity") == "High"
    )

    medium = sum(
        1 for threat in threats
        if threat.get("severity") == "Medium"
    )

    low = sum(
        1 for threat in threats
        if threat.get("severity") == "Low"
    )

    total = len(threats)

    score = round(
        (
            (critical * 4)
            + (high * 3)
            + (medium * 2)
            + low
        )
        / (total * 4)
        * 100
    )

    if score >= 75:
        risk_level = "HIGH"

    elif score >= 50:
        risk_level = "MEDIUM"

    else:
        risk_level = "LOW"

    country_counter = Counter(
        threat.get("country", "Unknown")
        for threat in threats
    )

    attack_counter = Counter(
        threat.get("type", "Unknown")
        for threat in threats
    )

    top_country = country_counter.most_common(1)[0][0]

    top_attack = attack_counter.most_common(1)[0][0]

    if risk_level == "HIGH":

        recommendation = (
            "Immediate investigation recommended. "
            "Block suspicious IP addresses, monitor network traffic, "
            "and prioritize all Critical severity incidents."
        )

    elif risk_level == "MEDIUM":

        recommendation = (
            "Continue monitoring threat activity and investigate "
            "High severity alerts."
        )

    else:

        recommendation = (
            "Threat activity is currently low. Continue routine monitoring."
        )

    return {

        "threat_score": score,

        "risk_level": risk_level,

        "recommendation": recommendation,

        "top_country": top_country,

        "top_attack": top_attack,

        "critical_count": critical,

        "high_count": high,

        "medium_count": medium,

        "low_count": low,

    }