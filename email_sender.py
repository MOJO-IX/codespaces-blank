import smtplib
import time

# Your email credentials
sender_email = "engashraf692@gmail.com"  # Your email address
password = "Ashraf92%"  # Your email password

# List of recipient email addresses
recipient_emails = [
    "list of emails"]

# Your CV file path
cv_path = "cv path"

# SMTP server configuration
smtp_server = "your SMTP"
smtp_port = 587 

# Establish a connection to the SMTP server
server = smtplib.SMTP(smtp_server, smtp_port)
server.starttls()
server.login(sender_email, password)

# Send the CV to each recipient
for recipient_email in recipient_emails:
    # Create the email message
    message = f"""\
        type
    """

    # Open and read the CV file
    with open(cv_path, "rb") as attachment:
        cv_content = attachment.read()

    # Add the CV as an attachment
    message = f"{message}\n\n"
    message = f"{message}{cv_content}"

    # Send the email
    server.sendmail(sender_email, recipient_email, message)

    print(f"CV sent to {recipient_email}")
    
    # Wait for 5 seconds before sending the next email
    time.sleep(5)

# Close the connection to the SMTP server
server.quit()

print("All emails sent successfully!")
