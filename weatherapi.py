#import request
import requests

#define api endpoint and key
base_url = "https://api.openweathermap.org/data/2.5/weather"
api_key = "1e37c0685e67dea375873e0bff4586b9"

#prompt user to enter city name
city = input ("Enter City name:")

#endpoint url
url = f"{base_url}?q={city}&appid={api_key}"

#http get to endpoint
response = requests.get(url)

#check code status
if response.status_code == 200:
    data = response.json()
    temp_kelvin = data["main"]["temp"]
    temp_celsius = temp_kelvin - 273
    temp_farenheit = (temp_celsius * 18) + 32
    weather = data["weather"][0]["description"]
    wind_speed = data["wind"]["speed"]

    #display weather data
    print(f"current weather in {city}")
    print(f"Temperature: {temp_celsius:.2f} degrees celsius / {temp_farenheit:.2f} Farenheit ")
    print(f"weather description : {weather}")
    print(f"wind speed : {wind_speed} m/s")

else:
     print("Error accessing API:", response.status_code)

