#!/usr/bin/python

import socket
import smtplib

# Sender and Receiver
sender = ['??']
receivers = ['??']


# Create your password(.txt) file and message(.txt) file
'''
with open('password.txt', 'r') as f:
    password = f.read()

with open('message.txt', 'r') as f:
    message = f.read()
'''

# \\ Optional [don't forget to remove "<>" at password]
'''
password = <ur password>  

message = """
            From: ? <??>

            To: ? <??>

            Subject: SMTP e-mail test
          """
'''

try:

   smtpObj = smtplib.SMTP('??')         
   smtpObj.login ('??', password)
   smtpObj.sendmail(sender, receivers, message)
   print("Successfully sent email")

except BaseException:
    print('Error: Unable to send email.')
    
