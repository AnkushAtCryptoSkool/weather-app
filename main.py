import requests
import json
import pyttsx3

engine = pyttsx3.init()
country = input("Enter the name of country who weather details you want to see or hear :\n")
city = input("Enter the name of city who weather details you want to see or hear :\n")
url = f"http://api.weatherapi.com/v1/current.json?key=92bded793aa649198f372553252601&q={country}&q={city}"
response = requests.get(url)

print(response.text)
weather_dict = json.loads(response.text)
currTemp = weather_dict["current"]["temp_c"]
statement = f"Current Tempreature of {city},{country} is {currTemp} degree celcius"
print(statement)
engine.say(statement)
engine.runAndWait()
