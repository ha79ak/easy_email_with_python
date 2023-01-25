import smtplib
from email.message import EmailMessage

def easy_email():
    sub = input("Subject : ")
    body = input("Message : ")
    frm = input("Sender : ")
    to = ".....@gmail.com"

    msg = EmailMessage()
    msg.set_content(body)
    msg['subject'] = sub
    msg['to'] = to

    user = '......@gmail.com'
    msg['from'] = frm
    password = '.........' # do not add email password here, it should be google app password https://support.google.com/mail/answer/185833?hl=en

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(user, password)
        server.send_message(msg)
        server.quit()
    except smtplib.SMTPException:
        print('Error: unable to send email')

if __name__ == '__main__':
    easy_email()