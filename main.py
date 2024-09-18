from pprint import pprint

from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
ORIGINAL_LOCATION_CODE = "BTS"

data = DataManager()
pprint(data.sheet_data)

sheet_data = data.get_data()
pprint(f"sheet_data before\n{sheet_data}")
if len(sheet_data[0]["iataCode"]) == 0:
    from flight_search import FlightSearch
    flight_search = FlightSearch()

    for row in sheet_data:
        row["iataCode"] = flight_search.get_iata_code(row["city"])
        # flight_search.get_price(row["iataCode"])
#
data.sheet_data = sheet_data
data.update_iata_code()
print("Updated ", sheet_data)


# print('data.sheet data', data.sheet_data)
# for row in data.sheet_data:
# fl_s = FlightSearch()
#
# for row in sheet_data:
#     prices_response = fl_s.get_price(row["iataCode"], ORIGINAL_LOCATION_CODE)
#     if len(prices_response["data"]) > 0:
#         fl_data = FlightData(prices_response["data"])
#         min_price = fl_data.get_min_price()
#         print(f"Min price for {row["city"]} is {min_price}")
#     else:
#         print(f"Sorry, there are not tickets for {row["city"]}")






