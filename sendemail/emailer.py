import os
import smtplib
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.utils import COMMASPACE

EMAIL_FROM='ivanovs223@gmail.com'
# EMAIL_TO=('ivanovs223@gmail.com', 'ivanovs.code@gmail.com')
EMAIL_TO='ivanovs223@gmail.com'


msg = MIMEMultipart()
msg['From'] = 'ivanovs223@gmail.com'
# msg['To'] = COMMASPACE.join(EMAIL_TO)
msg['To'] = COMMASPACE.join(EMAIL_TO)
msg['Subject'] = 'This is a test email from python'


for f in [f for f in os.listdir('.') if '.pdf' in f]:
    part = MIMEApplication(open(f, 'rb').read())
    msg.attach(part)


# to send
# on Mac OS to start smtp server: sudo postfix start
# on Mac OS to stop smtp server: sudo postfix stop
server = smtplib.SMTP("localhost", 25)
server.sendmail(EMAIL_FROM, EMAIL_TO, msg.as_string())
server.quit()