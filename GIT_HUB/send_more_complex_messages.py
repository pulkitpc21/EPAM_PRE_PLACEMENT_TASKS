import os   #To access environment variables
import smtplib  #library with two classes to send mails one is SMTP and other: SMTP_SSL


add = os.environ.get('TEMP_MAIL_ID')    #getting mail_id from environment
password = os.environ.get('TEMP_MAIL_PASSWORD') #getting password from environment
'''

                                      #port_number
with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:    #USING SMTP class  and with is used as context manager so that we do not have to close the connection

    smtp.login(add,password) #logging in

    subject = "Hello World!!"
    body = "How are you?"

    msg = f'Subject:{subject}\n{body}'    #F-string formatting for subject and body. We have to leave lines between them that is why \n\n\
                                            #if not left then it adds body to subject as continuation

    smtp.sendmail(add,'<recipient_mail_id>',msg)  #sending mail(sender,receiver,message)
'''

from email.message import EmailMessage


msg = EmailMessage()            #better formatting of message
msg['Subject'] = "Hello World!!"
msg['From'] = add
msg['To'] = '<recipient_mail_id>'
msg.set_content("How are you?")


with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:    #USING SMTP class  and with is used as context manager so that we do not have to close the connection

    smtp.login(add,password) #logging in

    smtp.send_message(msg)  #sending_message(message) because from and to had been added to msg only
    


