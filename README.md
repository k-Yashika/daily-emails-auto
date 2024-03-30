# Daily Email Report Automation

This project automates the process of sending daily email reports using Python. It utilizes the "smtplib" library for sending emails and the 'schedule' library for scheduling daily reports.

## Features

- Sends daily email reports at a specified time
- Easily configurable email settings
- Automatic scheduling and sending of reports
- Lightweight and simple set up

## Installation

1. Clone the repository:

   ```
   git clone https://github.com/k-Yashika/daily-emails-auto.git
   ```
3. Install dependencies:

   ```
   pip install secure-smtplib schedule
   ```

## Configuration

Before running the script, you need to configure the email settings:
- Open 'daily_emails.py' in a text editor
- Replace placeholders in the script with your actual email configuration
- Update the sender and receiver email addresses
- Update the SMTP server address, port, username, and password

## Usage

1. Run the script:

```
python daily_emails.py
```
3. The script will start runnign and will automatically send the email report at the specified time

## Customization

You can customize the script according to your requirements:
- Modify the email content in the 'send_email' function
- Change the scheduled time for sending the daily report in the 'setup_daily_email' function
- Adjust the frequency of checking for scheduled tasdks (default is every minute) by modifying the 'time.sleep' interval

## Contributing

Contributions are always welcome! If there is a mistake, or any suggetions, feel free to open an issue or create a pull request.

## License

This project is licensed under the MIT License

## Acknowledgements

- Python - Programming language used
- smtplib - Library for sending emails
- schedule - Library for scheduling tasks

