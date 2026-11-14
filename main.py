import os
import requests
import smtplib
from email.message import EmailMessage

from dotenv import load_dotenv

topic = input("Enter topic you are interested in: ")

load_dotenv()
NEWS_API_KEY = os.getenv("NEWS_API_KEY")
GMAIL_APP_PASSWORD = os.getenv("GMAIL_APP_PASSWORD")
GMAIL_USER = os.getenv("GMAIL_USER")
TO_ADDRESS = os.getenv("GMAIL_USER")

# Get data from API
url = (f"https://newsapi.org/v2/everything?q={topic}&from=2026-10-14"
       f"&apiKey={NEWS_API_KEY}")
response = requests.get(url)
data = response.json()

# Build the email body from every article
body_parts = []
for article in data["articles"]:
    title = article["title"] or ""
    description = article["description"] or ""
    body_parts.append(f"Title:\n{title}\n\nDescription:\n{description}")

body = ("\n\n" + "-" * 140 + "\n\n").join(body_parts)

# Build email message
msg = EmailMessage()
msg["Subject"] = f"News about {topic}"
msg["From"] = GMAIL_USER
msg["To"] = TO_ADDRESS
msg.set_content(body)

# Send the email
with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
    server.login(GMAIL_USER, GMAIL_APP_PASSWORD)
    server.send_message(msg)

print("Email sent.")
