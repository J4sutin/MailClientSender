import smtplib
# import threading
from socket import *
from socketserver import *
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

smtpObj = smtplib.SMTP('Insert', 25)

smtpObj.ehlo()

# // Create a password(.txt) file
with open('password.txt', 'r') as f:
    password = f.read()

smtpObj.login ('Insert', password)

msg = MIMEMultipart()

msg ['From'] = 'Insert'
msg ['To'] = 'Insert email'
msg ['Subject'] = 'Test only'

# // Create a message(.txt) file
with open('message.txt', 'r') as f:
    message = f.read()

msg.attach(MIMEText(message, 'plain'))

filename = 'Insert'
attachment = open(filename, 'rb')

p = MIMEBase('application', 'octet-stream')
p.set_payload(attachment.read())

encoders.encode_base64(p)
p.add_header('Content-Disposition'), f'attachment; filename={filename}'
msg.attach(p)

text = msg.as_string()
smtpObj.sendmail('Insert email', 'Insert email', text)

# Threading (don't mind) 
'''
Thread = []

for i in range(10):
    threading.Thread(target=filename)
    threading.daemon = True
    threading.Thread()

for index in range():
    threading.Thread[(start)]

for index in range():
    threading.Thread[(join)]
'''
