import json
import random
from datetime import datetime, timedelta

countries = [
    ("United States", "New York", 40.7128, -74.0060),
    ("India", "Mumbai", 19.0760, 72.8777),
    ("United Kingdom", "London", 51.5074, -0.1278),
    ("Germany", "Berlin", 52.5200, 13.4050),
    ("Japan", "Tokyo", 35.6762, 139.6503),
    ("Singapore", "Singapore", 1.3521, 103.8198),
    ("Australia", "Sydney", -33.8688, 151.2093),
    ("Canada", "Toronto", 43.6532, -79.3832),
    ("Brazil", "São Paulo", -23.5505, -46.6333),
    ("France", "Paris", 48.8566, 2.3522),
    ("Netherlands", "Amsterdam", 52.3676, 4.9041),
    ("South Korea", "Seoul", 37.5665, 126.9780),
]

attack_types = [
    "Phishing",
    "Malware",
    "Botnet",
    "Brute Force",
    "DDoS",
    "Ransomware",
    "SQL Injection",
    "Credential Stuffing",
]

severity_weights = {
    "Critical": 0.05,
    "High": 0.15,
    "Medium": 0.35,
    "Low": 0.45,
}


def random_ip():
    return ".".join(str(random.randint(1, 254)) for _ in range(4))


def random_severity():
    return random.choices(
        list(severity_weights.keys()),
        weights=list(severity_weights.values()),
        k=1,
    )[0]


data = []

for _ in range(1500):

    country, city, lat, lon = random.choice(countries)

    timestamp = (
        datetime.utcnow() -
        timedelta(minutes=random.randint(0, 10080))
    ).strftime("%Y-%m-%d %H:%M:%S UTC")

    data.append({
        "timestamp": timestamp,
        "ip": random_ip(),
        "country": country,
        "city": city,
        "latitude": lat,
        "longitude": lon,
        "severity": random_severity(),
        "type": random.choice(attack_types),
        "status": random.choice([
            "Blocked",
            "Investigating",
            "Mitigated"
        ]),
    })

with open("static/data/sample_threats.json", "w") as f:
    json.dump(data, f, indent=4)

print("Generated 1500 realistic threat records.")