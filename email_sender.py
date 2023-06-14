from email.message import EmailMessage
import ssl
import smtplib

email_sender = 'sendersemail@gmail.com'
email_password = 'your password'

email_reciever = 'anyemailreciever@gmail.com'
subject = 'This is the subject of the email'
body = "This is the body of the email"

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_reciever
em['subject'] = subject
em['body'] = body
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender,email_password)
    smtp.sendmail(email_sender, email_reciever,em.as_string())
