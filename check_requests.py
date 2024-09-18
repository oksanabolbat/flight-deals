import requests
from pprint import pprint

# URL = "https://api.sheety.co/5e301afd361699f385562a2287ee1c71/flightDeals/prices"
# TOKEN = "sometokenItIs23njk8"
# header = {
#     "Authorization": f"Bearer {TOKEN}"
# }
# URL = "https://api.sheety.co/1f35fcee30d9ea1d5cf0c396068544a3/flightsDeals/prices"
# TOKEN = "bhjdioaYu7s9wjhJKNXKkhdbckdsssaksacsall98"
# header = {
#     "Authorization": f"Bearer {TOKEN}"
# }
# get_response = requests.get(url=URL, headers=header)

# get_response = {'prices': [{'city': 'Paris', 'iataCode': '', 'id': 2, 'lowestPrice': 54},
#                            {'city': 'Frankfurt', 'iataCode': '', 'id': 3, 'lowestPrice': 42},
#                            {'city': 'Tokyo', 'iataCode': '', 'id': 4, 'lowestPrice': 485},
#                            {'city': 'Hong Kong', 'iataCode': '', 'id': 5, 'lowestPrice': 551},
#                            {'city': 'Istanbul', 'iataCode': '', 'id': 6, 'lowestPrice': 95},
#                            {'city': 'Kuala Lumpur',
#                             'iataCode': '',
#                             'id': 7,
#                             'lowestPrice': 414},
#                            {'city': 'New York', 'iataCode': '', 'id': 8, 'lowestPrice': 240},
#                            {'city': 'San Francisco',
#                             'iataCode': '',
#                             'id': 9,
#                             'lowestPrice': 260},
#                            {'city': 'Dublin', 'iataCode': '', 'id': 10, 'lowestPrice': 378}]}
#
# data = get_response["prices"]

# data = get_response.json()
# pprint(data)
# put_response = requests.put(url=f"{URL}/5", json={"price": {"iataCode": "TTT"}}, headers=header)
# print(put_response.text)

from flight_search import FlightSearch

flight_search = FlightSearch()
flight_search.get_iata_code('paris')
