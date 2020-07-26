import os   #To access environment variables
import smtplib  #library with two classes to send mails one is SMTP and other: SMTP_SSL

add = os.environ.get('TEMP_MAIL_ID')    #getting mail_id from environment
password = os.environ.get('TEMP_MAIL_PASSWORD') #getting password from environment


'''

with smtplib.SMTP('smtp.gmail.com',587) as smtp:    #USING SMTP class  and with is used as context manager so that we do not have to close the connection
    smtp.ehlo()             #sends the server a connection request(i.e. identifies itself to gmail.com)
    smtp.starttls()         #encrypts the connection
    smtp.ehlo()             #sends the server a connection request after encrypting(i.e. identifies itself to gmail.com)

    smtp.login(add,password) #logging in

    subject = "Hello World!!"
    body = "How are you?"

    msg = f'Subject:{subject}\n{body}'    #F-string formatting for subject and body. We have to leave lines between them that is why \n\n\
                                            #if not left then it adds body to subject as continuation

    smtp.sendmail(add,'<recipient_mail_id>',msg)  #sending message(sender,receiver,message)

'''
#to send mail to local server(to debug and not to receive mail on your id everytime)

with smtplib.SMTP('localhost',1025) as smtp:    #USING SMTP class  and with is used as context manager so that we do not have to close the connection

    subject = "Hello World!!"
    body = "How are you?"

    msg = f'Subject:{subject}\n{body}'    #F-string formatting for subject and body. We have to leave lines between them that is why \n\n\
                                            #if not left then it adds body to subject as continuation

    smtp.sendmail(add,'<recipient_mail_id>',msg)  #sending message(sender,receiver,message)
