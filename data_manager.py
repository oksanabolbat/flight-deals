# This class is responsible for talking to Google Sheet
import requests
import os

from dotenv import load_dotenv
load_dotenv()


class DataManager:
    def __init__(self):
        # self.sheet_data = self.get_data()

        self.sheet_url = os.getenv("URL")
        self.token = os.getenv("TOKEN")
        self.sheet_data = {}
        self.header = {
            "Authorization": f"Bearer {self.token}"
        }

    def get_data(self):
        # response = requests.get(url=self.sheet_url, headers=self.header)
        # pprint(response.json())
        resp_json = {'prices': [{'city': 'Paris', 'iataCode': '', 'id': 2, 'lowestPrice': 54},
                                {'city': 'Frankfurt', 'iataCode': '', 'id': 3, 'lowestPrice': 42},
                                {'city': 'Tokyo', 'iataCode': '', 'id': 4, 'lowestPrice': 485},
                                {'city': 'Hong Kong', 'iataCode': '', 'id': 5, 'lowestPrice': 551},
                                {'city': 'Istanbul', 'iataCode': '', 'id': 6, 'lowestPrice': 95},
                                {'city': 'Kuala Lumpur',
                                 'iataCode': '',
                                 'id': 7,
                                 'lowestPrice': 414},
                                {'city': 'New York', 'iataCode': '', 'id': 8, 'lowestPrice': 240},
                                {'city': 'San Francisco',
                                 'iataCode': '',
                                 'id': 9,
                                 'lowestPrice': 260},
                                {'city': 'Dublin', 'iataCode': '', 'id': 10, 'lowestPrice': 378}]}
        # return response.json()["prices"]
        return resp_json["prices"]

    def update_iata_code(self):
        print("update self", self.sheet_data)
        for destination in self.sheet_data:
            new_data = {"price": {"iataCode": destination["iataCode"]}}
            print("DEST ", destination["id"])
            response = requests.put(url=f"{self.sheet_url}/{destination["id"]}", json=new_data, headers=self.header)
            print(response.text)
