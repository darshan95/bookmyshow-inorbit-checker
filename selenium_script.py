#Running script using selenium
import sys
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import smtplib
from email.mime.text import MIMEText

url = "http://goo.gl/S3Ovtc"
username = "<usename>"
password = "<password>"
sender = '<sender_email>'
receivers = ['<list of receivers emails'>]
message = MIMEText("""Head over here to check if the script worked correctly. :P
http://goo.gl/QGibm3""")
message['Subject'] = "Yo!!. We are on for Inoribt - monday - mission-impossible-rogue-nation :D"
message['From'] = "GoGoMaster<GoGoMaster@GoGo.com>"
message['To'] = ", ".join(receivers)
smtpObj = smtplib.SMTP('smtp.gmail.com:587')

while True:
	driver = webdriver.Firefox()
	driver.get("url")
	assert "Mission" in driver.title
	content = driver.find_elements_by_class_name('listing')
	tosearchfor = "Inorbit Mall"
	for element in content:
		if tosearchfor in element.text:
			smtpObj.ehlo()
			smtpObj.starttls()
			smtpObj.login(username, password)
			smtpObj.sendmail(sender, receivers, message.as_string())
			smtpObj.quit()
			print "Successfully sent email"
			driver.quit()
			sys.exit()
	time.sleep(5)
	driver.quit()