import imapclient
import pyzmail

imapObj = imapclient.IMAPClient('imap.gmail.com', ssl = True)
imapObj.login('valery.voitova@gmail.com', 'hrbottest2206')
imapObj.select_folder('Candidates', readonly = True)
UIDs = imapObj.search(['UNANSWERED'])
rawMessages = imapObj.fetch(UIDs, ['BODY[]'])
print(rawMessages)

for key, rawMessage in rawMessages.items():
    message = pyzmail.PyzMessage.factory(rawMessage[b'BODY[]'])
    message_body = message.text_part.get_payload().decode(message.text_part.charset)
    print(message_body)
