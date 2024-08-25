import requests
import smtplib
import time
from datetime import datetime

MY_LAT = 17.886190
MY_LONG = 83.446342
MAIL = "//gmail.com"
PASSWORD = "//"


response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

#Your position is within +5 or -5 degrees of the ISS position.


def is_near():
    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5:
        return True
    return False


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()
hour_time = int(time_now.hour)
# to check for every 60 seconds of time
while True:
    time.sleep(60)
    if is_near():
        if hour_time >= sunset or hour_time <= sunrise:
            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=MAIL, password=PASSWORD)
                connection.sendmail(
                    from_addr=MAIL,
                    to_addrs="others mail",
                    msg="subject:LOOK UP!\n\nthe iss is above you in the sky"
                )




