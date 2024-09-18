# This class is responsible for structuring the flight data

class FlightData:
    def __init__(self, prices_response):
        self.prices_response = prices_response

    def get_min_price(self):
        prices = [float(data["price"]["total"]) for data in self.prices_response]
        return min(prices)
