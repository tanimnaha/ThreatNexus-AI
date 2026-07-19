import json
from datetime import datetime


THREAT_FILE = "static/data/sample_threats.json"


def get_live_threat_feed(limit=10):
    """
    Returns the latest threat records sorted by timestamp.
    """

    try:

        with open(THREAT_FILE, "r") as file:
            threats = json.load(file)

    except (FileNotFoundError, json.JSONDecodeError):

        return []

    # Convert timestamp to datetime for proper sorting
    for threat in threats:

        try:

            threat["_datetime"] = datetime.fromisoformat(
                threat["timestamp"]
            )

        except Exception:

            threat["_datetime"] = datetime.min

    # Sort newest first
    threats.sort(
        key=lambda threat: threat["_datetime"],
        reverse=True
    )

    latest_threats = []

    for threat in threats[:limit]:

        latest_threats.append({

            "timestamp": threat.get("timestamp", "N/A"),

            "ip": threat.get("ip", "Unknown"),

            "country": threat.get("country", "Unknown"),

            "city": threat.get("city", "Unknown"),

            "severity": threat.get("severity", "Low"),

            "type": threat.get("type", "Unknown"),

            "status": threat.get("status", "Active")

        })

    return latest_threats