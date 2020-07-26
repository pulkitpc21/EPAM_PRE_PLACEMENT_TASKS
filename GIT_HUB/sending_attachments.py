import os   #To access environment variables
import smtplib  #library with two classes to send mails one is SMTP and other: SMTP_SSL


add = os.environ.get('TEMP_MAIL_ID')    #getting mail_id from environment
password = os.environ.get('TEMP_MAIL_PASSWORD') #getting password from environment

from email.message import EmailMessage


msg = EmailMessage()            #better formatting of message
msg['Subject'] = "Adding Attachments"
msg['From'] = add
msg['To'] = '<recipient_mail_id>'
msg.set_content("Images below...")

files = ["contacts.xls"]

import imghdr


for file in files:
    with open(file,'rb') as f:

        file_data = f.read()
        #file_type = imghdr.what(f.name)
        file_name = f.name

    msg.add_attachment(file_data,maintype = "application", subtype = "octet-stream", filename = file_name)



        

with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:    #USING SMTP class  and with is used as context manager so that we do not have to close the connection

    smtp.login(add,password) #logging in

    smtp.send_message(msg)  #sending_message(message) because from and to had been added to msg only
    
