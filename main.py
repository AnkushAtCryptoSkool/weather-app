import requests
import json
import pyttsx3
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv(dotenv_path="properties.env")

engine = pyttsx3.init()

# Get user inputs
country = input("Enter the name of the country whose weather details you want to see or hear:\n")
city = input("Enter the name of the city whose weather details you want to see or hear:\n")

# Retrieve API key from environment variable
api_key = os.getenv('WEATHER_API_KEY')

print("API Key fetched:", api_key)
# Correct URL by combining city and country properly
location = f"{city},{country}"
url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={location}"

# Make the request
response = requests.get(url)

# Check for successful response
try:
    weather_dict = json.loads(response.text)

    if "current" in weather_dict:
        curr_temp = weather_dict["current"]["temp_c"]
        statement = f"Current temperature of {city}, {country} is {curr_temp} degrees Celsius."
        print(statement)
        engine.say(statement)
        engine.runAndWait()
    else:
        print("Error fetching weather details. Please check the city name or API key. Response:", weather_dict)

except Exception as e:
    print("An error occurred while processing the weather data:", e)
