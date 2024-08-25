import requests
from datetime import datetime
MY_LAT = 17.886190
MY_LNG = 83.446342
# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# data = response.json()
# longitude = data["iss_position"]["longitude"]
# latitude = data["iss_position"]["latitude"]
# iss_position = (latitude, longitude)
# print(iss_position)

parameters = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted": 0
}


response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
# response.raise_for_status() to check the response from server whether it was successful or not
data = response.json()
sun_rise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sun_set = data["results"]["sunset"].split("T")[1].split(":")[0]
print(sun_rise)

now = datetime.now()
hour_time = now.hour
print(hour_time)