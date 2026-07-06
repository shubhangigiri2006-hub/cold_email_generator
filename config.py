import os
from dotenv import load_dotenv

load_dotenv()

# ---------------- LLM (Groq - free) ----------------
GROQ_API_KEY = os.getenv("GROQ_API_KEY","")
GROQ_MODEL = os.getenv("GROQ_MODEL", "llama-3.3-70b-versatile")

# ---------------- Web search ----------------
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY","")
# ---------------- Admin auth (placeholder) ----------------
ADMIN_USERNAME = os.getenv("ADMIN_USERNAME", "")
ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD", "")

# ---------------- SMTP ----------------
SMTP_HOST = os.getenv("SMTP_HOST", "smtp.gmail.com")
SMTP_PORT = int(os.getenv("SMTP_PORT", "587"))
SMTP_USER = os.getenv("SMTP_USER", "")
SMTP_PASSWORD = os.getenv("SMTP_PASSWORD", "")

# ---------------- Organization profile ----------------
ORG_PROFILE = {
    "name": os.getenv("ORG_NAME", "Your Organization"),
    "website": os.getenv("ORG_WEBSITE", ""),
    "services": os.getenv("ORG_SERVICES", ""),
    "description": os.getenv("ORG_DESCRIPTION", ""),
    "sender_name": os.getenv("ORG_SENDER_NAME", "Admin"),
    "sender_title": os.getenv("ORG_SENDER_TITLE", "Business Development"),
}

MAX_REVIEW_ITERATIONS = 3