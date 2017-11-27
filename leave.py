#!/usr/bin/env python

# Python code to send leave email with today's date
import smtplib
import constants
import datetime
import email
from email.mime.text import MIMEText

# list of email_id to send the mail
now = datetime.datetime.now()

message = email.MIMEMultipart.MIMEMultipart()
message['From'] = constants.FROM
message['To'] = ', '.join(constants.LEAVE_TO)
message['Date'] = email.Utils.formatdate(localtime=True)
message['Subject'] = "On Leave, " +  now.strftime("%d/%m/%Y")

message.attach(MIMEText(constants.LEAVE_BODY))

smtpserver = smtplib.SMTP('smtp.gmail.com', 587)
smtpserver.ehlo()
smtpserver.starttls()
smtpserver.ehlo
smtpserver.login(constants.USERNAME, constants.PASSWORD)
smtpserver.sendmail(constants.FROM, constants.LEAVE_TO, message.as_string())
print 'Leave email sent'
smtpserver.quit()
