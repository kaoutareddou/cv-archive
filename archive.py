import datetime
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import dropbox


def compile_latex():
    os.system('pdflatex template.tex')


def upload_cv_and_get_shared_link():
    access_token = os.environ['DROPBOX_ACCESS_TOKEN']

    dbx = dropbox.Dropbox(access_token)

    d = datetime.datetime.today()

    file_from = 'template.pdf'
    file_to = f'/CV_El-Mehdi-ASSALI_{d.strftime("%d-%m-%YT%H:%M:%S")}.pdf'

    with open(file_from, 'rb') as f:
        dbx.files_upload(f.read(), file_to)

        shared_link_metadata = dbx.sharing_create_shared_link_with_settings(file_to)

        return shared_link_metadata.url


def send_email(shared_link):
    mail_content = f'''
    A new version of your CV is available.

    You can access your CV via: {shared_link}.
    '''

    sender_address = 'cv.archive.km@gmail.com'
    sender_pass = os.environ['EMAIL_PASSWORD']

    receiver_address = 'assalielmehdi@gmail.com'

    message = MIMEMultipart()

    message['From'] = sender_address
    message['To'] = receiver_address
    message['Subject'] = '[CV-ARCHIVE] New CV'

    message.attach(MIMEText(mail_content, 'plain'))

    session = smtplib.SMTP('smtp.gmail.com', 587)

    session.starttls()
    session.login(sender_address, sender_pass)

    text = message.as_string()

    session.sendmail(sender_address, receiver_address, text)

    session.quit()


def main():
    compile_latex()

    shared_link = upload_cv_and_get_shared_link()

    send_email(shared_link)


if __name__ == '__main__':
    main()
