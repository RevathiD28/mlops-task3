import smtplib
import urllib.request as urllib

# Senders and receivers email
sender = "mlopstask3@gmail.com"
rec = "revathii.d28@gmail.com"

#This message will apppear in the mail
msg = "The model is trained"

#SMTP object is going to be used for connection with the server. Port for TLS/STARTTLS
server = smtplib.SMTP('smtp.gmail.com', 587)

# Start the server connection
server.starttls()

# Login
server.login("mlopstask3@gmail.com", "mlops12345")
print("Logged in Successfully!")

# Send Email
server.sendmail("Revathi", {revathii.d28@gmail.com}, msg)
print("Email has been sent successfully to {receiver}")