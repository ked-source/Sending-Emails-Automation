# Sending-Emails-Automation

Automated Email Sender
This script allows you to send automated emails using a Python script. It utilizes the smtplib library to establish a secure connection with the SMTP server (in this case, Gmail's SMTP server) and sends emails to the specified recipient.

Prerequisites
Before running the script, ensure you have the following:
-Python 3 installed on your machine.
-An active Gmail account for sending emails. Make sure to enable "Less Secure Apps" access in your Gmail account settings.
 Installation
-Clone the repository or download the email_automation.py file.

Install the required dependencies using the following command:
pip install smtplib

Usage
Open the email_automation.py file in a text editor.

Set up the email parameters:
sender_email: Your Gmail email address.
sender_password: Your Gmail account password.
receiver_email: The email address of the recipient.
subject: The subject of the email.
message: The content of the email.
Save the changes.

Run the script using the following command:
python email_automation.py

The script will establish a secure connection with the SMTP server, log in to your Gmail account, send the email, and display a success message or an error message if something goes wrong.
