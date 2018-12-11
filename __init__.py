import imapclient
import pyzmail

def get_emails_body():
    imapObj = imapclient.IMAPClient('imap.gmail.com', ssl = True)
    imapObj.login('valery.voitova@gmail.com', 'hrbottest2206')
    imapObj.select_folder('Candidates', readonly = True)
    UIDs = imapObj.search(['UNANSWERED'])
    rawMessages = imapObj.fetch(UIDs, ['BODY[]'])

    def parse_raw_emails():
        message = pyzmail.PyzMessage.factory(rawMessages['BODY'])
        print(message)

get_emails_body()