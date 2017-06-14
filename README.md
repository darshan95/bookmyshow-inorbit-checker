There are 2 python scripts in this repository, which primarily polls bookmyshow in every **5 seconds** to check if **PVR:Cyberabad, Inorbit Mall** is listed for **Mission Impossible - Rogue Nation, Monday show** (these informations are taken care of in URL which is shortened using https://goo.gl/).  

The scripts are:  
1. ***urllib_script.py:*** It uses **urllib2** to poll bookmyshow.  
2. ***selenium_script.py:*** It uses **selenium** to poll bookmyshow.  


Once the URL is opened using **urllib2** (in urllib_script.py) or **selenium** (in selenium_script.py), one can search easily for presence of **Inorbit Mall**.    
After the match is found, mail is sent to concerned persons using **smtplib** package. **Gmail** smtp server is used, which is available for free. More details here: [Link](https://support.google.com/a/answer/176600?hl=en)   

*******adfasfasfasf
