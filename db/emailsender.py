import smtplib, ssl


dummy_message = """
Hi Nadav!
This is Eevee, you personal productivity assistant.
This is the api gateway for the signup lambda function:
https://5268gn05lh.execute-api.eu-central-1.amazonaws.com/default/signup
"""

smtp_server = "smtp.gmail.com"
port = 465
sender_email = "eeveeproductivity@gmail.com"
password = "eevee_prod_22"
context = ssl.create_default_context()
#server = smtplib.SMTP(smtp_server, port)
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email,"weisler.nadav@gmail.com",dummy_message)
