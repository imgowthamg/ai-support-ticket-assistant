# 🎫 AI Support Ticket Assistant

An Agentic AI-powered support ticket analysis system built using **CrewAI**, **FastAPI**, **Streamlit**, **SQLite**, and **Docker**.

## 🚀 Features

* Ticket Classification
* Priority Assessment
* Solution Recommendation
* Escalation Decision
* Team Assignment
* Knowledge Base Lookup using SQLite
* Streamlit Dashboard
* Dockerized Deployment

---

## 🏗️ Architecture

```text
User
 │
 ▼
Streamlit UI
 │
 ▼
FastAPI Backend
 │
 ▼
CrewAI Agents
 ├── Classifier Agent
 ├── Priority Agent
 ├── Resolver Agent
 └── Escalation Agent
 │
 ▼
SQLite Knowledge Base
```

---

## 🛠️ Tech Stack

| Component             | Technology |
| --------------------- | ---------- |
| Backend API           | FastAPI    |
| Multi-Agent Framework | CrewAI     |
| Frontend              | Streamlit  |
| Database              | SQLite     |
| Containerization      | Docker     |
| Language              | Python     |

---

## 📂 Project Structure

```text
support-ticket-ai/
│
├── app/
│   ├── agents/
│   ├── api/
│   ├── crew/
│   ├── database/
│   ├── models/
│   └── main.py
│
├── streamlit_app.py
├── requirements.txt
├── Dockerfile
├── start.sh
├── .env.example
└── README.md
```

---

## ⚙️ Environment Variables

Create a `.env` file in the project root.

```env
OPENAI_API_KEY=your_openai_api_key_here
```

Never commit your actual API key to GitHub.

---

## 🔧 Installation

### Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/ai-support-ticket-assistant.git

cd ai-support-ticket-assistant
```

### Create Virtual Environment

```bash
python -m venv venv

source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Create Environment File

```bash
cp .env.example .env
```

Edit `.env` and add your OpenAI API key.

---

## ▶️ Run Locally

### Start FastAPI

```bash
uvicorn app.main:app --reload
```

Swagger UI:

```text
http://localhost:8000/docs
```

### Start Streamlit

```bash
streamlit run streamlit_app.py
```

Streamlit Dashboard:

```text
http://localhost:8501
```

---

## 🐳 Docker Deployment

### Build Docker Image

```bash
docker build -t support-ticket-ai .
```

### Run Docker Container

```bash
docker run \
-e OPENAI_API_KEY="your_openai_api_key_here" \
-p 8000:8000 \
-p 8501:8501 \
support-ticket-ai
```

---

## 🧪 Sample Ticket

```text
Payment failed after entering card details
```

### Sample Response

```json
{
  "category": "Payment",
  "priority": "High",
  "solution": "Verify card details and retry payment.",
  "escalate": true,
  "assigned_team": "Payments Support"
}
```
<img width="1875" height="928" alt="Screenshot from 2026-06-01 10-55-52" src="https://github.com/user-attachments/assets/51362035-92f6-472f-9146-3170e4fd6580" />

---

## 🎯 Future Enhancements

* LangGraph Integration
* RAG with Vector Database
* AWS Deployment
* Email Notifications
* Slack Integration
* Human-in-the-loop Approval
* Analytics Dashboard

---

## 💼 Skills Demonstrated

* Multi-Agent AI Systems
* CrewAI Workflow Design
* FastAPI Development
* REST API Design
* SQLite Database Management
* Docker Containerization
* Streamlit UI Development
* AI-powered Automation

---

## 📜 License

MIT License

Feel free to fork, modify, and extend this project.
