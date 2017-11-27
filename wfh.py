#!/usr/bin/env python

# Python code to illustrate Sending mail 
# to multiple users 
# from your Gmail account 
import smtplib
import constants
from random import randint
import email
from email.mime.text import MIMEText
 
# list of email_id to send the mail
message = email.MIMEMultipart.MIMEMultipart()
message['From'] = constants.FROM
message['To'] = ', '.join(constants.WFH_TO)
message['Date'] = email.Utils.formatdate(localtime=True)
message['Subject'] = "Work From Home"
message.attach(MIMEText(constants.EXCUSES[randint(0, len(constants.EXCUSES))]))

smtpserver = smtplib.SMTP('smtp.gmail.com', 587)
smtpserver.ehlo()
smtpserver.starttls()
smtpserver.ehlo
smtpserver.login(constants.USERNAME, constants.PASSWORD)
smtpserver.sendmail(constants.FROM, constants.WFH_TO, message.as_string())
print 'WFH Email Sent'
smtpserver.quit()
