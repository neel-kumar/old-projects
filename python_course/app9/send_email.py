from email.mime.text import MIMEText
import smtplib

def send_email(email, height, average_height, count):
    from_email = "dumbobodboy@gmail.com"
    from_password = "9yfokguf"
    to_email = email

    subject = "Height Data"
    message = "Hey there your height is <strong>%s</strong>cm. <br> Average height of all is <strong>%s</strong>, that is calculated out of <strong>%s</strong>. <br Thanks!>" % (height, average_height, (count + 1))
    msg = MIMEText(message, 'html')
    msg['Subject'] = subject
    msg['To'] = to_email
    msg['From'] = from_email

    gmail = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    gmail.ehlo()
    gmail.login(from_email, from_password)
    gmail.send_message(msg)
