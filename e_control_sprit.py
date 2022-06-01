"""
 # @ Author: Alex
 # @ Create Time: 2022-05-20 19:35:26
 # @ Modified by: Alex
 # @ Modified time: 2022-05-24 08:07:13
 # @ Description:
 """

import json
from http import client


class Request:
    """Request class"""

    def __init__(self, url: str, request_string: str) -> None:
        self.url = url
        self.request_string = request_string
        self.conn = client.HTTPSConnection(self.url)

    def get_data(self) -> str:
        """returns the data from the request"""
        self.conn.request(
            "GET",
            self.request_string,
        )
        return json.loads(self.conn.getresponse().read().decode())

    def get_formated_json(self) -> str:
        """returns the formated json from the request

        Returns:
            str: formated json string
        """
        return json.dumps(self.get_data(), indent=4, sort_keys=True)


Sprit = Request(
    "api.e-control.at",
    "/sprit/1.0/search/gas-stations/by-region?code=312&type=PB&fuelType=SUP",
)

print(Sprit.get_formated_json())
