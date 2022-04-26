import datetime
import smtplib 
from tkinter import messagebox
from email.mime.multipart import MIMEMultipart 

from email.mime.text import MIMEText 

from email.mime.base import MIMEBase 

from email import encoders 
def sendMail():
        
        fromaddr = "manasamulukutla@gmail.com"

        toaddr = "manasamulukutla@gmail.com"

        
        # instance of MIMEMultipart 

        msg = MIMEMultipart() 

        
        # storing the senders email address   

        msg['From'] = fromaddr 

        
        # storing the receivers email address  

        msg['To'] = toaddr 

        
        # storing the subject  

        msg['Subject'] = "PythonMail"

        
        # string to store the body of the mail 

        body = "hi! I am hereby sending an attatchment"

        
        # attach the body with the msg instance 

        msg.attach(MIMEText(body, 'plain')) 

        
        # open the file to be sent  
        l=[str(current_time.day),str(current_time.month),str(current_time.year)]
        l="-".join(l)
        
        filename = l+".xlsx"

        attachment = open(filename, "rb") 

        
        # instance of MIMEBase and named as p 

        p = MIMEBase('application', 'octet-stream') 

        
        # To change the payload into encoded form 
        p.set_payload((attachment).read()) 

        
        # encode into base64 
        encoders.encode_base64(p) 

        

        p.add_header('Content-Disposition', "attachment; filename= %s" % filename) 

        
        # attach the instance 'p' to instance 'msg' 
        msg.attach(p) 

        #messagebox.showinfo("Success","Sending Mail")
        # creates SMTP session 

        s = smtplib.SMTP('smtp.gmail.com', 587) 

        
        # start TLS for security 
        s.starttls() 

        
        # Authentication 

        s.login(fromaddr, "mjmanasa") 

        
        # Converts the Multipart msg into a string 

        text = msg.as_string() 

        
        # sending the mail 
        s.sendmail(fromaddr, toaddr, text) 
        
        
        # terminating the session 
        s.quit() 
        #messagebox.showinfo("Success","Successfully sent")
        print("Done!") 
current_time = datetime.datetime.now()
print(current_time.hour)
if current_time.hour==18 and current_time.minute==00:
    sendMail()
    