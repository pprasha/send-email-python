import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
def setup():
    print("Welcome to send-email-python to get stated with gmail please turn on less secure apps in gmail settings.")
    return "Done"
class email():
    def __init__(self, sender_email = None, sender_password = None, reciever_email = None, subject = None, message = None):
        self.sender_email = sender_email
        self.sender_password = sender_password
        self.reciever_email = reciever_email
        self.subject = subject
        self.message = message
    def send(self):
        msg = MIMEMultipart()
        msg['From'] = self.sender_email
        msg['To'] = self.reciever_email
        msg['Subject'] = self.subject
        msg.attach(MIMEText(self.message, 'plain'))
        try:
            server = smtplib.SMTP("smtp.gmail.com",587)
            # server.ehlo() # Can be omitted
            server.starttls() # Secure the connection
            # server.ehlo() # Can be omitted
            server.login(self.sender_email, self.sender_password)
            server.sendmail(self.sender_email, self.reciever_email, msg.as_string())
            return "Passed"
        except Exception as e:
            # Print any error messages to stdout
            print(e)
        finally:
            server.quit()             





