import imapclient
import pyzmail

def get_emails_body():
    imapObj = imapclient.IMAPClient('imap.gmail.com', ssl = True)
    imapObj.login('valery.voitova@gmail.com', 'hrbottest2206')
    imapObj.select_folder('Candidates', readonly = False)
    UIDs = imapObj.search(['UNANSWERED'])
    rawMessages = imapObj.fetch(UIDs, ['BODY[]'])

    message = pyzmail.PyzMessage.factory(rawMessages['BODY'])
    message_body = message.text_part.get_payload().decode(message.text_part.charset)
    print(message_body)

get_emails_body()
