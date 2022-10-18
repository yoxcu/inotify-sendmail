#!/usr/bin/python
#Do Not Modify
#---------------------------------------------------------
import os,sys
import glob
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime
#---------------------------------------------------------

#script settings
monitorPath=sys.argv[1]
oldScanPath=monitorPath+"/.oldScan"

#email server settings
port = 587  # For starttls
smtp_server = "server.domain.de"
sender_email = "user@domain.de"
receiver_email = "user@domain.de"
password = 'passwort'

#email content
subject="Neue oder veränderte Dateien gefunden"
text = """\
Es wurden {number} neue oder geänderte Dateien gefunden:
Datei                    \tÄnderungsdatum
{files}"""
html = ""

#per "row" formatting
txtRowFormat="{filename:<25}\t{timestamp}"
htmlRowFormat="{filename:<25}\t{timestamp}"

#misc settings
debug=False
sendMailOnFirst=False

#Do Not Modify
#---------------------------------------------------------
import os
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime



def send_mail(text,html):
    message = MIMEMultipart("alternative")
    message["Subject"] = subject
    message["From"] = sender_email
    message["To"] = receiver_email

    part1 = MIMEText(text, "plain", "utf-8")
    message.attach(part1)
    if html != "":
        part2 = MIMEText(html, "html")
        message.attach(part2) 

    context = ssl.create_default_context()
    with smtplib.SMTP(smtp_server, port) as server:
        res=server.starttls(context=context)
        if debug:
            print(res)
        res=server.login(sender_email, password)
        if debug:
            print(res)
        res=server.sendmail(sender_email, receiver_email, message.as_string())
        if debug:
            print(res)


if debug:
    print("Looking for .oldScan in {}".format(oldScanPath))
oldScan=[]
if (os.path.isfile(oldScanPath)):
    if debug:
        print("oldScan found")
    sendMailOnFirst=True
    with open(oldScanPath,"r") as f:
        for line in f.readlines():
            oldScan.append(line.strip("\n").split(","))

if debug:
    print("Scanning {}".format(monitorPath))
files = []
for file in glob.iglob(monitorPath + '**/**', recursive=True):
    if file != monitorPath and file != oldScanPath:
        files.append([file[len(monitorPath)+1:],str(os.path.getmtime(file))])
if debug:
    print("Found Files:\n{}".format(files))

modifiedFiles = []
for file in files:
    if not file in oldScan:
        modifiedFiles.append(file)

if debug:
    print("Detected modified Files:\n".format(modifiedFiles))

with open(oldScanPath,"w") as f:
    f.write("\n".join([",".join(x) for x in files]))

if len(modifiedFiles) >= 1:
    if debug:
        print("Preparing Mail:")
    msg=text.format(number=len(modifiedFiles),files="\n".join([txtRowFormat.format(filename=x[0],timestamp=datetime.fromtimestamp(float(x[1])).strftime('%Y-%m-%d %H:%M:%S'))  for x in modifiedFiles]))
    msgHtml=html.format(number=len(modifiedFiles),files="\n".join([htmlRowFormat.format(filename=x[0],timestamp=datetime.fromtimestamp(float(x[1])).strftime('%Y-%m-%d %H:%M:%S'))  for x in modifiedFiles]))
    if debug:
        print(msg,msgHtml)
    if sendMailOnFirst:
        send_mail(msg,msgHtml)
