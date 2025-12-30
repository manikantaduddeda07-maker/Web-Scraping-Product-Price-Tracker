import requests
from bs4 import BeautifulSoup
import re
import json
import csv
import smtplib
import os
from email.mime.text import MIMEText
from datetime import datetime
from dotenv import load_dotenv

# =========================
# LOAD ENV & CONFIG
# =========================
load_dotenv()

EMAIL_SENDER = os.getenv("EMAIL_SENDER")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
EMAIL_RECEIVER = os.getenv("EMAIL_RECEIVER")

with open("config.json", "r") as f:
    config = json.load(f)

TARGET_PRICE = config["target_price"]

# =========================
# CONFIG
# =========================
URL = "<Enter_product_url>"
# =========================
# Enter only flipkart product url here   
# =========================
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

# =========================
# FETCH HTML
# =========================
response = requests.get(URL, headers=HEADERS)
if response.status_code != 200:
    raise Exception("❌ Failed to fetch page")

soup = BeautifulSoup(response.text, "html.parser")

# =========================
# EXTRACT TITLE
# =========================
title_tag = soup.find("meta", property="og:title")
product_title = title_tag["content"]

# =========================
# EXTRACT PRICE
# =========================
price_tag = soup.find("div", class_="hZ3P6w bnqy13")
raw_price = price_tag.get_text(strip=True)
current_price = int(re.sub(r"[^\d]", "", raw_price))

# =========================
# COMPARE PRICE
# =========================
alert_triggered = current_price <= TARGET_PRICE
alert_status = "YES" if alert_triggered else "NO"

# =========================
# LOG TO CSV
# =========================
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

with open("prices.csv", "a", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow([
        timestamp,
        product_title,
        current_price,
        TARGET_PRICE,
        URL,
        alert_status
    ])

# =========================
# SEND EMAIL (ONLY IF ALERT)
# =========================
if alert_triggered:
    subject = "🚨 Price Drop Alert!"
    body = f"""
Product: {product_title}
Current Price: ₹{current_price}
Target Price: ₹{TARGET_PRICE}

Buy now:
{URL}
"""

    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = EMAIL_SENDER
    msg["To"] = EMAIL_RECEIVER

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(EMAIL_SENDER, EMAIL_PASSWORD)
        server.send_message(msg)

    print("\n📧 Email alert sent successfully!")

else:
    print("\nℹ️ No email sent. Price above target.")
