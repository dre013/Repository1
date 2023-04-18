from email.message import EmailMessage
from password_gmail import password
import ssl
import smtplib

email_sender = 'nice.andrey013@gmail.com'
email_password = password

email_receiver = 'Почта получателя'

subject = 'Send me money'
body = '''
When you read this message, send me $100
'''

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['Subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())