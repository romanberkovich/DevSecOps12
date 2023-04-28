
# CREATE A PYTHON SCRIPT THAT AUTOMATES THE PROCESS OF SENDING EMAILS. THE SCRIPT SHOULD:
# 1. PROMPT THE USER FOR THE RECIPIENT'S EMAIL ADDRESS, SUBJECT, AND MESSAGE.
# 2. CONNECT TO THE EMAIL SERVER USING SMTP (SIMPLE MAIL TRANSFER PROTOCOL).
# 3. AUTHENTICATE THE USER USING THEIR EMAIL ADDRESS AND PASSWORD.
# 4. COMPOSE THE EMAIL MESSAGE WITH THE GIVEN SUBJECT AND MESSAGE.
# 5. SEND THE EMAIL TO THE SPECIFIED RECIPIENT.

import smtplib
import time

email_adress = input('Hello, Please Enter The Your Mail Address: ')
email_password = input('Please Enter The Password Of Your Email Address: ')
recipient_email_adress = input('Please Enter Recipient Email:')
email_subject = input('Please Enter The Subject Of Your Email: ')
compose_email = input('Please Compose Your Email: ')
# Replace port and email domain  with your email ( outlook = 587, gmail = 587, yahoo = 465, walla = 587 )
email_server = smtplib.SMTP('smtp.gmail.com' , 587)
email_server.starttls()
email_server.login(email_adress , email_password)
message_subject = f'Subject: {email_subject}\n\n{compose_email}'
email_server.sendmail(email_adress, recipient_email_adress , message_subject )

print('Connecting to the server....')
time.sleep(7)
print('Email sent successfully!')
email_server.quit()
