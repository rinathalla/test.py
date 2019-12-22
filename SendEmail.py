import smtplib
conn = smtplib.SMTP('smtp.gmail.com', 587)   #call smtp functn calling domain(server) name & port
type(conn)     #
#<class 'smtplib.SMTP'>
conn
#< smtplib.SMTP object at 0x06062630 >
conn.ehlo()            #To connect to smtp server
#(250,b'smtp.gmail.com at your service, [45.114.192.211]\nSIZE 35882577\n8BITMIME\nSTARTTLS\nENHANCEDSTATUSCODES\nPIPELINING\nCHUNKING\nSMTPUTF8')
conn.starttls()  #begin encryptn or password will be encrypted
conn.login('rina.thalla@wellnessforever.in','Well#370549')  #Login credentials
conn.sendmail('rina.thalla@wellnessforever.in','rinathalla6@gmail.com','Subject : Test Mail..\n\n Dear Rina,\nHello,this is a test mail')  #Send Mail

conn.quit()