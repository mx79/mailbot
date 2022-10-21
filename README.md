# MailBot

## What can you do with this project ?

You can email a lookup table without to add receiver one by one like on Outlook or Gmail.

## How it works ?

This MailBot is very easy to use but there is no web interface for the moment.

You just have to have basic Python understanding.

There is 4 little steps before sending your email to multiple receiver.

1) Load you credentials to connect to your address in a .env file at project's root 

Structure is the following :
- EMAIL="your_email_address"
- PASSWORD="your_password"

Make sure you have changer the server of your mail address in smtplib.SMTP('SMTP.office365.com') or smtplib.SMTP('SMTP.gmail.com')

2) Change the subject and the message of msg["Subject"] and msg.set_content()

3) Attach eventual file with load_attachment() function

4) And of course fill the mail list of the file mail.csv after "mails" column name

That's all, you can now run the script main.py and your mail must be sent to every mail address instantiate in mail.csv.

Script will panic if there are any problem.
