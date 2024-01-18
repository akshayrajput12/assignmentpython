'''1.	Weather App:
Develop a Python program that retrieves weather information using an API and displays it to the user. Allow users to input a city and get the current weather conditions
'''
import requests

def get_weather(city):
    api_key = "your_api_key"
    base_url = "http://api.openweathermap.org/data/2.5/weather"

    complete_url = base_url + "appid=" + api_key + "&q=" + city

    response = requests.get(complete_url)

    if response.status_code == 200:
        data = response.json()
        main = data['weather'][0]['main']
        description = data['weather'][0]['description']
        temp = data['main']['temp']

        return f"Weather: {main}\nDescription: {description}\nTemperature: {temp}K"
    else:
        return f"Error: Invalid city name. HTTP Response Code: {response.status_code}"

def main():
    city = input("Enter the city name: ")
    weather_data = get_weather(city)
    print(weather_data)

if __name__ == "__main__":
    main()
