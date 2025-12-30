# Price Tracker – Flipkart (Python Automation)
A simple Python-based price tracking tool that monitors a Flipkart product’s price, logs price history, and sends an email alert when the price drops below a user-defined target.
The script can be automated to run daily using Windows Task Scheduler or Linux cron.

## 🚀 What This Project Does
Scrapes a Flipkart product page
Extracts the current price
Compares it with a target price
Logs every run into a CSV file
Sends an email alert when the target price is reached
Can be automatically scheduled (daily, hourly, etc.)
This project is designed as a standalone automation tool, not a hosted web application.

## 🧩 Project Structure
price_tracker/ │ ├── price_tracker.py # Main script ├── config.json # User-defined target price ├── prices.csv # Auto-generated price history ├── .env # Email configuration template ├── .gitignore # Ignores .env file └── README.md # Documentation

## 🛠 Requirements
Python 3.9 or above
Internet connection
A Gmail account (for email alerts)
Python Libraries Used
requests
beautifulsoup4
python-dotenv
Install them using:
```bash
pip install requests beautifulsoup4 python-dotenv
```
## 🔧 Initial Setup (Step-by-Step)
### 1️⃣ Clone the Repository
```bash
git clone <your-repo-url>
cd price_tracker
```
### 2️⃣ Configure Email (Required)
For security reasons, email credentials are not included in the repository. Each user must configure their own email credentials locally.

Create .env file you can look at the example .env file that i have provided

Fill in your details as shown in file

Important notes:

- Use a Gmail App Password, not your regular Gmail password
- How to find Gmail App Password follow the following steps
- Open Manage your Google Account < security & sign in
- Enable 2-Step Verification in your Google account
- Search App Password in the search bar (not the main search bar)
- click the App Password < Enter the name of the app > (use "Mail" default )
- copy the alphabets and paste in the .env file respectively
### 3️⃣ Set Target Price
Open config.json and set your desired target price:

### 4️⃣ Set Product URL
Open price_tracker.py and update the product URL:

Current limitations:

- Only Flipkart product pages are supported
- Only one product can be tracked at a time
### 5️⃣ Run the Script Manually (First-Time Test)
Before automating, always test the script manually:
```bash
python price_tracker.py
```
### 6️⃣ Verify Output
Check Terminal Output

- Product title and current price should be printed
- Alert message appears only if price ≤ target price
- Check prices.csv
        - A new row should be appended in this format: timestamp,title,current_price,target_price,url,alert

- Check Email Inbox
        - An email alert is sent only if the target price condition is met
        - No email is sent if the price is above the target
## 🛠 Automate the Script 🪟 Windows – Task Scheduler

Step 1 : click win search Task Scheduler, Open Task Scheduler ;

Step 2 : Click Create Task

Step 3 : In the General tab:

Name the task (e.g., Price Tracker – Daily)
Description: Daily price tracking with email alerts
check Run whether user is logged on or not
Check Run with highest privileges
Step 4 : In the Triggers tab:

click New
Set trigger to Daily
Set time to 00:00
Recur every: 1 day
Enabled ✔
OK
Step 5 : In the Actions tab:

click New
Program/script: (C:\Users\sriha\AppData\Local\Programs\Python\Python310\python.exe)
Add arguments: <Enter .py file name> (price_tracker.py)
Start in : <Enter .py file path >
Step 6 : Conditions tab

Uncheck Start only if AC power
Uncheck Stop on battery
Step 7 : Save the task , Now click OK. NOW Windows WILL ask for your login password , This is normal and required.

Step 8 : it askes for User ID password (just for configuration the scheduler)

### Limitations
Supports Flipkart only
Tracks one product at a time
Requires manual email configuration
Designed as a standalone automation tool, not a hosted service
### Why This Project Exists
This project demonstrates: 
- Web scraping fundamentals
- Automation scripting
- Secure credential handling
- OS-level scheduling
- Real-world problem solving
  It is designed as a developer-friendly automation tool, not a consumer application.
### Repository cloned successfully (if you want to clone and confirm it success)
.env file configured with email credentials
config.json target price set
Product URL updated in price_tracker.py
Script runs manually without errors
prices.csv updates correctly
Email alert received when price condition is met
Script scheduled successfully (Windows or Linux) If all the above are satisfied, the project is fully configured and operational.
