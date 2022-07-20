import requests
import config
from pprint import pprint


print("\nWelcome to the Weather Data Fetcher")

# taking required input from user
print("\nWould you like to enter\n1. Co-ordinates\n2. City name")
while True:
    user_choice = int(input("\nEnter 1 or 2: "))
    if user_choice == 1:
        latitude = input("\nEnter latitude: ")
        longitude = input("Enter longitude: ")
        break
    elif user_choice == 2:
        city_name = input("Enter city name: ")
        
        # When city name is provided as input, its co-ordinates
        # are obtained using Geo-coding API
        def fetch_coords(city):
            BASE_URL = "http://api.openweathermap.org/geo/1.0/direct"
            response = requests.get(f"{BASE_URL}?appid={config.API_KEY}&q={city}")
            if response.status_code == 200:
                data = response.json()
                return [data[0]['lat'], data[0]['lon']]
        latitude, longitude = fetch_coords(city_name)
        break
    else:
        print("Please type either 1 or 2.")
        continue
    

def fetch_weather(lat, lon):
    BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
    response = requests.get(f"{BASE_URL}?appid={config.API_KEY}&lat={lat}&lon={lon}")
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print("An error has occurred.")

    
weather_data = fetch_weather(latitude, longitude)
print()
print(f"City: {weather_data['name']}")
print(f"Country code: {weather_data['sys']['country']}")
print(f"Co-ordinates: {weather_data['coord']['lat']}, {weather_data['coord']['lon']}")
print(f"\nWeather: {weather_data['weather'][0]['description']}")
print(f"Humidity: {weather_data['main']['humidity']}%")
print(f"Atmospheric Pressure: {weather_data['main']['pressure']} hPa")
print(f"Temperature: {(weather_data['main']['temp'] - 273.15):.2f}°C")



    

 


