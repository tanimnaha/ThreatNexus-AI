# 🛡️ ThreatNexus AI

> **AI-Powered Cyber Threat Intelligence Dashboard** built using **Flask**, **Python**, **Plotly**, **SQLite**, and **VirusTotal API** to visualize cyber threats, perform IOC lookups, analyze attack patterns, and generate security reports.

---

## 📌 Project Overview

ThreatNexus AI is a web-based Cyber Threat Intelligence (CTI) dashboard that simulates a modern Security Operations Center (SOC). The application provides interactive dashboards, threat analytics, IOC (Indicator of Compromise) lookup using the VirusTotal API, live threat monitoring, and downloadable reports.

This project demonstrates the practical implementation of cybersecurity concepts, data visualization, API integration, and Flask web development.

---

# ✨ Features

- 🌍 Global Threat Intelligence Dashboard
- 🔍 VirusTotal IOC Lookup (IP & Domain)
- 🛡️ AI-Based Threat Risk Assessment
- 📊 Interactive Security Analytics
- 📈 Threat Timeline Visualization
- 📉 Threat Severity Distribution
- 🌐 Top Targeted Countries Analysis
- 🎯 Attack Type Distribution
- 📡 Live Threat Feed
- 📄 CSV Report Export
- 📑 PDF Report Export
- ⚡ Auto Dashboard Refresh
- 📱 Responsive User Interface

---

# 🛠️ Tech Stack

| Category | Technology |
|-----------|------------|
| Backend | Python, Flask |
| Frontend | HTML5, CSS3, JavaScript |
| Database | SQLite |
| Visualization | Plotly |
| API | VirusTotal API v3 |
| Data Processing | Pandas |
| Reporting | ReportLab |

---

# 📂 Project Structure

```text
ThreatNexus-AI/
│
├── app/
├── templates/
├── static/
├── database/
├── screenshots/
├── app.py
├── config.py
├── requirements.txt
└── README.md
```

---


# ⚙️ Installation

## 1. Clone the repository

```bash
git clone https://github.com/tanimnaha/ThreatNexus-AI.git
```

## 2. Navigate to the project folder

```bash
cd ThreatNexus-AI
```

## 3. Install the required dependencies

```bash
pip install -r requirements.txt
```

## 4. Configure the VirusTotal API Key

Open **config.py** and add your VirusTotal API Key.

## 5. Run the application

```bash
python app.py
```

## 6. Open your browser

```text
http://127.0.0.1:5000
```

---

# 📌 Application Modules

- 🏠 Home
- 📊 Dashboard
- 📈 Analytics
- 📄 Reports
- ℹ️ About

---

# 🔐 VirusTotal Integration

ThreatNexus AI integrates with the VirusTotal API to perform IOC lookups.

Supported lookups include:

- IP Address
- Domain
- Reputation Score
- Malicious Count
- Suspicious Count
- Harmless Count
- ASN
- Network Information
- Country
- Analysis Statistics
- Tags

---

# 📊 Dataset

The application uses a realistic cybersecurity dataset containing approximately **1,500 simulated threat records**, including:

- Attack Type
- Severity Level
- Country
- City
- Timestamp
- IP Address
- Threat Status

---

# 🎯 Learning Outcomes

This project demonstrates practical knowledge of:

- Cyber Threat Intelligence (CTI)
- Flask Web Development
- REST API Integration
- VirusTotal API
- Interactive Dashboard Development
- Data Visualization using Plotly
- SQLite Database Management
- Report Generation
- Cybersecurity Data Analysis

---

# 🚀 Future Improvements

- User Authentication
- Real-time Threat Intelligence APIs
- Machine Learning-Based Threat Prediction
- Docker Deployment
- Cloud Deployment (AWS/Azure)
- Email Alert System

---

# 👨‍💻 Developer

**Tanim Naha**

B.Tech in Computer Science & Engineering

Amity University Kolkata

📧 Email: nahatanim6@gmail.com

🔗 GitHub: https://github.com/tanimnaha

💼 LinkedIn: https://www.linkedin.com/in/tanimnaha/

---

# ⭐ Support

If you found this project helpful, consider giving it a **⭐ Star** on GitHub.

---

# 📜 License

This project is developed for **educational and portfolio purposes**.
