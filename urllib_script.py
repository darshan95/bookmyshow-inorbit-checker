#Running script using urllib2
import sys
import time
import urllib2
from BeautifulSoup import BeautifulSoup
import re
import smtplib
from email.mime.text import MIMEText

url = #<Movie's link where all theatres are present>
username = #<username>
password = #<password>
sender = #<sender's email>
receivers = [<List of people whom you want to send>]
message = MIMEText("""Head over here to check if the script worked correctly. :P
<link of movie>"")
message['Subject'] = "Yo!!. We are on :D"
message['From'] = "GoGoMaster<GoGoMaster@GoGo.com>"
message['To'] = ", ".join(receivers)
#Yes, google has a open SMTP server :D
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