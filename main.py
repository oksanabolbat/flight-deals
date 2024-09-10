from pprint import pprint

from data_manager import DataManager


data = DataManager()
pprint(data.sheet_data)

sheet_data = data.get_data()
pprint(f"sheet_data before\n{sheet_data}")
if len(sheet_data[0]["iataCode"]) == 0:
    print("inside if [0]", sheet_data[0])
    from flight_search import FlightSearch
    flight_search = FlightSearch()

    for row in sheet_data:
        row["iataCode"] = flight_search.get_iata_code(row["city"])
        print(row["iataCode"])

pprint(f"sheet_data\n{sheet_data}")
data.sheet_data = sheet_data
data.update_iata_code()
