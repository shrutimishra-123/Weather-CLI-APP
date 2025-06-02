import requests

API_KEY = 932bdfeccc2add5872307053af3af4ec
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
	params = {
		"q": city,
		"appid": API_KEY,
		"units": "metric"
	}

	response = requests.get(BASE_URL, params=params)

	if response.status_code == 200:
		data = response.json()
		temp = data['main']['temp']
		desc = data['weather'][0]['description']
		print(f"Weather in {city.capitalize()}: {temp}°C, {desc}")
	else:
		print("City not found. Please check the name and try again.")

if __name__ == "__main__":
	city = input("Enter city name: ")
		get_weatehr(city)