import requests
import os
from twilio.rest import Client  # to send SMS

API_ENDPOINT = "https://api.openweathermap.org/data/2.5/weather"
API_KEY = os.environ.get('OWM_API_KEY')
MY_LAT = 29.697790
MY_LON = -95.585190

parameters = {
    "lat": MY_LAT,
    "lon": MY_LON,
    "appid": API_KEY
}

print(parameters)

response = requests.get(url=API_ENDPOINT, params=parameters)
response.raise_for_status()
weather_data = response.json()["weather"][0]

print(weather_data)

# parameters for twilio
ACCOUNT_SID = os.environ.get("TWILLIO_SID")
AUTH_TOKEN = os.environ.get("TWILLIO_TOKEN")
FROM_NUM = "Twilio Num"
TO_NUM = "Your Num"

client = Client(ACCOUNT_SID, AUTH_TOKEN)

if weather_data["id"] < 700:
    message_body = "Will Rain Today. Bring out umbrella"
else:
    message_body = "Weather is find. Never-mind"

message = client.messages.create(body=message_body, from_=FROM_NUM, to=TO_NUM)
print(f"message.status = {message.status}\n error_code = {message.error_code}\n error_message = {message.error_message}")
