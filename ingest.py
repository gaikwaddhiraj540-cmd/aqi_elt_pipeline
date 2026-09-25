import requests
import os
TOKEN = os.environ.get("WAQI_TOKEN")

CITIES = ["delhi", "mumbai", "bengaluru", "chennai", "kolkata"]

def get_aqi(city):
    url = f"https://api.waqi.info/feed/{city}/"
    r = requests.get(url, params={"token": TOKEN})
    r.raise_for_status()
    return r.json()

def main():
    for city in CITIES:
        data = get_aqi(city)
        if data["status"] != "ok":
            print(f"{city}: {data.get('data')}")
            continue
        d = data["data"]
        print(f"\n{city.title()} — AQI: {d['aqi']} (dominant: {d.get('dominentpol')})")
        for pollutant, reading in d.get("iaqi", {}).items():
            print(f"  {pollutant}: {reading['v']}")

if __name__ == "__main__":
    main()