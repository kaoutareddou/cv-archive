import os
import smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

os.system('pdflatex template.tex')

mail_content = "This your cv's last version"

sender_address = 'cv.archive.km@gmail.com'
sender_pass = '******'

receiver_address = 'assalielmehdi@gmail.com'

message = MIMEMultipart()
message['From'] = sender_address
message['To'] = receiver_address
message['Subject'] = 'New CV has been built'

message.attach(MIMEText(mail_content, 'plain'))

attach_file_name = 'template.pdf'
attach_file = open(attach_file_name, 'rb')

payload = MIMEBase('application', 'octet-stream')
payload.set_payload(attach_file.read())
encoders.encode_base64(payload)

attach_file.close()

payload.add_header('Content-Decomposition', 'attachment', filename=attach_file_name)
message.attach(payload)

session = smtplib.SMTP('smtp.gmail.com', 587)
session.starttls()
session.login(sender_address, sender_pass)

text = message.as_string()

session.sendmail(sender_address, receiver_address, text)
session.quit()

print('Mail Sent')
