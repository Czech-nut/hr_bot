import smtplib
import time
import imaplib
import email

ORG_EMAIL = "@gmail.com"
FROM_EMAIL = "valery.voitova" + ORG_EMAIL
FROM_PWD = "hrbottest2206"
SMTP_SERVER = "imap.gmail.com"
SMTP_PORT = 993

def readmail():
    mail = imaplib.IMAP4_SSL(SMTP_SERVER)
    mail.login(FROM_EMAIL, FROM_PWD)
    mail.select('inbox')

    type, data = mail.search(None, 'ALL')      #searching for all incoming emails
    mail_ids = data[0]
    id_list = mail_ids.split()

    first_email_id = int(id_list[0])
    latest_email_id = int(id_list[-1])

    for i in range(latest_email_id, first_email_id, -1):
        type, data = mail.fetch(i, '(RFC822)')

        for response_part in data:
            if isinstance(response_part, tuple):
                msg = email.message_from_string(response_part[1])
                email_subject = msg['subject']
                email_from = msg['from']
                print
                'From : ' + email_from + '\n'
                print
                'Subject : ' + email_subject + '\n'