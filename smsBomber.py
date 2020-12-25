# import smtplib, time
# port = 587
# s_server='smtp.gmail.com'
# sender='meetgoyani245@gmail.com'
# # receiver='vdhvanik@gmail.com'
# receiver='18bce253@nirmauni.ac.in'
# password=input('Enter the password :')
# message='Hiiii mere dost'
# server=smtplib.SMTP(s_server,port)
# server.starttls()
# server.login(sender,password)
# for i in range(10):
# 	server.sendmail(sender,receiver,message)
# 	print('{} sent successfully'.format(i+1))
# 	time.sleep(1)
# server.sendmail(sender,receiver,'If you get this mail then whatsapp me.....')
# print('Task is completed............')

import smtplib 
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

port_number =8000
msg = MIMEMultipart()
msg['From'] = 'babubatlivala@protonmail.com'
msg['To'] = 'meetgoyani245@gmail.com'
msg['Subject'] = 'My Test Mail '
message = 'This is the body of the mail'
msg.attach(MIMEText(message))
mailserver = smtplib.SMTP('localhost',port_number)
mailserver.login("babubatlivala@protonmail.com", "qwertyudj")
mailserver.sendmail('babubatlivala@protonmail.com','meetgoyani245@gmail.com',msg.as_string())
mailserver.quit()