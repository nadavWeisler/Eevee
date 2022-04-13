import smtplib, ssl

def sendMail(name, receiver_email, message):
    smtp_server = "smtp.gmail.com"
    port = 465
    sender_email = "eeveeproductivity@gmail.com"
    password = "eevee_prod_22"
    context = ssl.create_default_context()
    #server = smtplib.SMTP(smtp_server, port)
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email,receiver_email, message)