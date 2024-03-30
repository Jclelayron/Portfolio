import smtplib,ssl
import os

def send_email(email, message_input,topic):
    host = "smtp.gmail.com"
    port = 465
    username=os.getenv("USER")
    password = os.getenv("PASSWORD")

    receiver = "jclelayron@gmail.com"
    context = ssl.create_default_context()

    message = f"Subject: Email Message from Portfolio\n\n"\
                f"Topic: {topic}\n"\
                f"{message_input}\n\n"\
                f"From: {email}"

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username,receiver,message)
