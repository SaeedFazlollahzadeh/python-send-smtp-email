import smtplib
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

sender_email = 'your_email@gmail.com'
receiver_email = input('Enter email address: ')
password = 'GIVEN PASSWORD'
# https://myaccount.google.com/apppasswords you should create an app here and paste given password up here
message = MIMEMultipart('alternative')
message['Subject'] = 'YOUR SUBJECT'
message['From'] = sender_email
message['To'] = receiver_email

# path and file to attach. Don't forget to change MIMEBase according to your file's mime type.
path = r'/path/to/'
file_name = r'your_file.pdf'
attachment = path + file_name
part = MIMEBase('application', "pdf")  # Don't forget to change MIMEBase according to your file's mime type.
part.set_payload(open(attachment, "rb").read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', 'attachment', filename=file_name)
message.attach(part)

# Create the plain-text and HTML version of your message
html = '''<p>Your HTML Codes go here</p>
<p>This is another HTML paragraph.'''
part1 = MIMEText(html, 'plain')
part2 = MIMEText(html, 'html')

# Add HTML/plain-text parts to MIMEMultipart message
# The email client will try to render the last part first
message.attach(part1)
message.attach(part2)

# Create secure connection with server and send email
context = ssl.create_default_context()
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(
        sender_email, receiver_email, message.as_string()
    )
