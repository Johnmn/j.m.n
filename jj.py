import smtplib 

try:
    # Set sender mail, receivers mail and messages
    sender_mail = "sender@domain.com"
    receivers_mail = ['receiver1@domain', 'receiver2@domain']
    to = ", ".join(receivers_mail)
    message = """Subject: Python testing mail This mail is sent using Python SMTP."""
    
    # Make SMTP connection
    obj = smtplib.SMTP('smtp.gmail.com', 587) 
  
    # secure with TLS
    obj.starttls() 
  
    # Mail Server Authentication
obj.login(USRENAME, PASSWORD) 
  
    # sending the mail 
    obj.sendmail(sender_mail, to, message) 
    print("Mail sent successfully.")
    
    # terminating the session 
    obj.quit()
    
except Exception:
    print("Mail delivery failed.")
