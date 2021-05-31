import smtplib, ssl


def handler():
    post = Postman()
    post.send()
    port = 587  # 465 for SMTP_SSL() // 587 for .starttls()
    host = "smtp.ionos.mx"
    sender = "admon@misever.com"
    receiver = "carloxdev@gmail.com"
    password = "Clave2021!"
    email_text = """\
        From: %s
        To: %s
        Subject: %s

        %s
        """ % (sender, ", ".join(receiver), "Hola Testing", "This is an example!")

    try:
        import pdb; pdb.set_trace()
        server = smtplib.SMTP(host, port)
        server.starttls()
        server.login(sender, password)
        server.sendmail(sender, receiver, email_text)

    except Exception as e:
        print(str(e))


    # Create a secure SSL context
    # context = ssl.create_default_context()

    # with smtplib.SMTP_SSL("smtp.ionos.mx", port, context=context) as server:
    #     server.login(sender, password)
    #     server.sendmail(sender, receiver, message)
    # print(f"Message Send to {receiver}")
