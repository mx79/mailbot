import smtplib
import mimetypes
import pandas as pd
from os import getenv
from pathlib import Path
from dotenv import load_dotenv
from email.utils import formatdate
from email.message import EmailMessage
from os.path import abspath, dirname, join


def load_attachment(filename: list = None):
    """
    Allow to send attachment to your email by simply giving filename stored at project's root.
    => load_attachment() or load_attachment(["your_file_1.txt", "your_file_2.csv"]) <=
    :param filename: List of the files you want to attach to your mail, None by default
    """
    if filename:
        for file in filename:
            cfile = Path(join(path, file))
            ctype, encoding = mimetypes.guess_type(cfile)
            if ctype is None or encoding is not None:
                ctype = 'application/octet-stream'
            maintype, subtype = ctype.split('/', 1)
            msg.add_attachment(cfile.read_bytes(), maintype=maintype, subtype=subtype, filename=cfile.name)


# Path
path = dirname(abspath(__file__))

# Load dotenv variable
load_dotenv(join(path, '.env'))

# Load mail list
mails = list(pd.read_csv(join(path, 'mail.csv'))['mails'])

# Server start and login with credentials
server = smtplib.SMTP('SMTP.office365.com', 587)
server.connect('SMTP.office365.com', 587)
server.ehlo()
server.starttls()
server.login(getenv("EMAIL"), getenv("PASSWORD"))

# Iterate through mails list
for mail in mails:
    email = mail.strip()
    # Headers : your personal address, date, subject, message
    msg = EmailMessage()
    msg['From'] = f'John Doe <{getenv("EMAIL")}>'
    msg['To'] = email
    msg["Date"] = formatdate(localtime=True)
    msg['Subject'] = 'Subject of your message'
    msg.set_content("""\
    Content message here.
    """)

    # Add some file name in this function if you want to attach files to your mail
    load_attachment()

    # Trying to send the message, catch if there are any error
    try:
        server.send_message(msg)
        print('{0} : send'.format(email))
    except smtplib.SMTPException as e:
        print('{0} : {1}'.format(email, e))
        exit(1)

# Quit server
server.quit()
