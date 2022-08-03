import requests

response = requests.get("https://api.weather.gov/gridpoints/BUF/77,66/forecast")

print("\n The Weather For Rochester NY Today:")
for x in response.json().get('properties').get('periods')[0:2]:
    print(f"\n {x.get('name')}: "
          f"\n Temperature: {str(x.get('temperature')) + ' ' + str(x.get('temperatureUnit'))}"
          f"\n Wind speed: {x.get('windSpeed')}"
          f"\n Forecast: {x.get('shortForecast')}")
