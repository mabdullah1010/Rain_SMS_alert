import requests
from twilio.rest import Client
import os


parameters = {
    "lat": "YOUR LATITUDE COORDINATES",
    "lon": "YOUR LONGITUDE COORDINATES",
    "appid": "318bc5e4f7e480e162084c81b244be74",
    "cnt": "4"
}

account_sid = os.environ["SID"]
auth_token = os.environ["AUTH"]

OWN_endpoint = "https://api.openweathermap.org/data/2.5/forecast"
response = requests.get(OWN_endpoint, params=parameters)
data = response.json()["list"]
will_rain = False
for hour in data:
    if hour["weather"][0]["id"] < 800:
        will_rain = True
    print(hour["weather"][0]["id"])

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It will rain tomorrow, carry an umbrella",
        from_="+12513254331",
        to= os.getenv("MY_PHONE_NUMBER"),
    )

print("check your messages")
c = input()
