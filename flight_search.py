# This class is responsible for Talking to the Flight Search API
# key jSFNV2jDQkhRN9JsqRoGyBS78mmOLi7J
# secret Fe7FbF06WukKVRoa
from dotenv import load_dotenv
import requests
import os
from pprint import pprint

load_dotenv()
amadeus_url = "https://test.api.amadeus.com/v1"
get_token_url = f"{amadeus_url}/security/oauth2/token"
get_code_url = f"{amadeus_url}/reference-data/locations/cities"


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

