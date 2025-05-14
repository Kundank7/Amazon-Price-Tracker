import requests
import smtplib
import os
import datetime as dt
from dotenv import load_dotenv
from bs4 import BeautifulSoup

alert = input("Enter Amazon Product Url")
URL = requests.get(alert)
response = URL.text

soup = BeautifulSoup(response, "html.parser")
price = soup.find(class_="a-offscreen").getText() 
np = str(price)
newp = np.split("$")[1]
print(newp)

load_dotenv()
my_mail = os.getenv("EMAIL_ADDRESS")
my_pass = os.getenv("EMAIL_PASSWORD")
my_smtp = os.getenv("SMTP_ADDRESS")

now = dt.datetime.now()
time = now.time()
print(time.hour)

alert_price = "$99.99"

if time.hour == 16:
    if price == alert_price:
        my_mail = my_mail
        my_pass = my_pass

        connection = smtplib.SMTP(my_smtp,port=587)
        connection.starttls()
        connection.login(user=my_mail, password=my_pass)
        connection.sendmail(from_addr=my_mail, to_addrs="myself100kk@gmail.com", msg=f"subject:Price Drop Alert \n\n Price Droped {price}")
        connection.close()
    else:
        print("Check Your Code")
