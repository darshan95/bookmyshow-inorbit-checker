#Running script using urllib2
import sys
import time
import urllib2
from BeautifulSoup import BeautifulSoup
import re
import smtplib
from email.mime.text import MIMEText

url = "http://goo.gl/S3Ovtc"
username = "sigegov.gov"
password = "sigegov123"
sender = 'sigegov.gov@gmail.com'
receivers = ['akash.agrawall094@gmail.com', 'shikher111@gmail.com', 'jaspreetsingh112@gmail.com']
message = MIMEText("""Head over here to check if the script worked correctly. :P
http://goo.gl/S3Ovtc""")
message['Subject'] = "Yo!!. We are on for Inoribt - monday - mission-impossible-rogue-nation :D"
message['From'] = "GoGoMaster<GoGoMaster@GoGo.com>"
message['To'] = ", ".join(receivers)

smtpObj = smtplib.SMTP('smtp.gmail.com:587')

while True:
	page = urllib2.urlopen(url).read()
	soup = BeautifulSoup(page)
	for element in soup.findAll(attrs = {'class': re.compile(r"listing")}):
		ele = element.findAll(text = re.compile("Inorbit"))
		if ele:
			smtpObj.ehlo()
			smtpObj.starttls()
			smtpObj.login(username, password)
			smtpObj.sendmail(sender, receivers, message.as_string())
			smtpObj.quit()
			print "Successfully sent email"
			sys.exit()
	time.sleep(5)