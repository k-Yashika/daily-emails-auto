import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import schedule
import time

def send_emails():
     sender = "your_email@example.com"
     receiver = "recipient@example.com"
     subject = "Daily Report"
     body = "Contents of your daily report"

     message = MIMEMultipart()
     message["From"] = sender
     message["To"] = receiver
     message["Subject"] = subject
     message.attach(MIMEText(body, "plain"))

     smtp_server = "smtp.example.com"
     smtp_port = 587
     smtp_username = "your_smtp_username"
     smtp_password = "your_smtp_password"

     with smtplib.SMTP(smtp_server, smtp_port) as server:
         server.starttls()
         server.login(smtp_username, smtp_password)
         text = message.as_string()
         server.sendmail(sender_email, receiver_email, text)

def setup_daily_email():
    schedule.every().day.at("10:00").do(send_email)

    while True:
        schedule.run_pending()
        time.sleep(60)

if __name__ == "__main__":
    setup_daily_email()
