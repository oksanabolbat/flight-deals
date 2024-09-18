# This class is responsible for Talking to the Flight Search API
# key jSFNV2jDQkhRN9JsqRoGyBS78mmOLi7J
# secret Fe7FbF06WukKVRoa
from dotenv import load_dotenv
import requests
import os
import datetime as dt
from pprint import pprint

load_dotenv()
amadeus_url = "https://test.api.amadeus.com/v1"
get_token_url = f"{amadeus_url}/security/oauth2/token"
get_code_url = f"{amadeus_url}/reference-data/locations/cities"

now = dt.datetime.now()

flight_date = now + dt.timedelta(days=100)
flight_date_str = flight_date.strftime("%Y-%m-%d")


class FlightSearch:
    def __init__(self):
        self._api_key = os.getenv("AMADEUS_KEY")
        self._api_secret = os.getenv("AMADEUS_SECRET")
        self._api_token = self._get_new_token()

    def _get_new_token(self):
        params = {
            "grant_type": "client_credentials",
            "client_id": self._api_key,
            "client_secret": self._api_secret
        }
        header = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        print(f"{self._api_key} \n {self._api_secret} ")
        response = requests.post(url=get_token_url, headers=header, data=params)
        # pprint(response.json())
        return response.json()["access_token"]

    def get_iata_code(self, city):
        print(city)
        params = {
            "keyword": city.upper()
        }
        header = {"Authorization": f"Bearer {self._api_token}"}
        try:
            code = requests.get(url=get_code_url, params=params, headers=header).json()["data"][0]["iataCode"]
        except IndexError:
            print(f"IndexError: no airport found for {city}")
            return "N/A"
        except KeyError:
            print(f"KeyError: no airport found for {city}")
            return "N/A"
        return code

    def get_price(self, city_code, original_location_code):
        header = {"Authorization": f"Bearer {self._api_token}"}
        params = {
            "originLocationCode": original_location_code,
            "destinationLocationCode": city_code,
            # "departureDate": flight_date_str,
            "departureDate": "2024-10-10",
            "adults": 1,
        }
        print("https://test.api.amadeus.com/v2/shopping/flight-offers", params, header)
        try:
            response = requests.get(url="https://test.api.amadeus.com/v2/shopping/flight-offers", params=params,
                                    headers=header)
            if response.status_code == 200:
                return response.json()
            else:
                return {"data": []}
        except KeyError:
            return {"data": []}

