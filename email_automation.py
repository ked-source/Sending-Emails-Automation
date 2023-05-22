import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(sender_email, sender_password, receiver_email, subject, message):
    # Create a multipart message and set the headers
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject

    # Add body to the email
    msg.attach(MIMEText(message, 'plain'))

    try:
        # Create a secure connection with the SMTP server
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        # Log in to the sender email account
        server.login(sender_email, sender_password)
        # Send the email
        server.send_message(msg)
        print("Email sent successfully!")
    except Exception as e:
        print(f"An error occurred while sending the email: {str(e)}")
    finally:
        # Close the SMTP server connection
        server.quit()

# Set up the email parameters
sender_email = "your_email@gmail.com"
sender_password = "your_password"
receiver_email = "recipient_email@example.com"
subject = "Automated Email"
message = "Hello, this email was sent using a Python script!"

# Send the email
send_email(sender_email, sender_password, receiver_email, subject, message)
