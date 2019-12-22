import imapclient

conn = imapclient.IMAPClient('imap.gmail.com', ssl=True)
conn.login('rina.thalla@wellnessforever.in', 'Well#370549')
# b'rina.thalla@wellnessforever.in authenticated (Success)'
conn.select_folder('INBOX', readonly=True)
# {b'PERMANENTFLAGS': (), b'FLAGS': (b'\\Answered', b'\\Flagged', b'\\Draft', b'\\Deleted', b'\\Seen', b'$NotPhishing', b'$Phishing'), b'UIDVALIDITY': 1, b'EXISTS': 657, b'RECENT': 0, b'UIDNEXT': 768, b'HIGHESTMODSEQ': 192330, b'READ-ONLY': [b'']}
UIDs = conn.search(['SINCE 05-Mar-2018']) #to find mail id till 5mar
UIDs
[40032, 40033, 40034, 40035, 40036, 40037, 40038, 40039, 40040, 40041]
rawMessages = conn.fetch([40041], ['BODY[]', 'FLAGS']) #searchng mail by id

"""#import pyzmail
#pyzmail.PyzMessage.factory(rawMessages[47474][b'BODY[]'])
#message = pyzmail.PyzMessage.factory(rawMessages[40041]['BODY[]'])
#message.get_subject()
'Hello!'
#message.get_addresses('from')
#[('Edward Snowden', 'esnowden@nsa.gov')]
#message.get_addresses('to')
[(Jane Doe', 'jdoe @ example.com')]
#message.get_addresses('cc')
 ##[]
 #message.get_addresses('bcc')
 []
 message.text_part != None
 True
 message.text_part.get_payload().decode(message.text_part.charset)
 #'Follow the money.\r\n\r\n-Ed\r\n'
 message.html_part != None
 True
 message.html_part.get_payload().decode(message.html_part.charset)
 #'<div dir="ltr"><div>So long, and thanks for all the fish!<br><br></div>-Al < br > < / div >\r\n'
conn.logout()"""
