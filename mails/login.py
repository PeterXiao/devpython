__author__ = 'Administrator'
import smtplib

GMAIL_USERNAME=''
GMAIL_PASSWORD=''
# The below code never changes, though obviously those variables need values.
session = smtplib.SMTP('smtp.gmail.com', 587)
session.ehlo()
session.starttls()
session.login(GMAIL_USERNAME, GMAIL_PASSWORD)

email_subject=''
recipient=''
headers = "\r\n".join(["from: " + GMAIL_USERNAME,
                       "subject: " + email_subject
                       "to: " + recipient,
                       "mime-version: 1.0",
                       "content-type: text/html"])

# body_of_email can be plaintext or html!
content = headers + "\r\n\r\n" + body_of_email
session.sendmail(GMAIL_USERNAME, recipient, content)