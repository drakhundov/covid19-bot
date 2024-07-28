import csv
from typing import List

import requests


class WebParser:
    def __init__(self, API_URL: str, args_lst: List):
        """
        API_URL must contain curly braces
        so that the class can format it
        with a token.
        """
        with open("m49.csv", "r") as m49_f:
            temp_m49 = list(csv.DictReader(m49_f))
        self.m49_map = {}
        for entry in temp_m49:
            self.m49_map[entry["Country"]] = entry["m49"]
        del temp_m49
        self.API_URL = API_URL
        self.args_lst = args_lst

    def parse(self, args):
        parse_url = f"{self.API_URL}?"
        for arg_name, arg_val in args.items():
            parse_url += f"{arg_name}={arg_val}"
        response = requests.get(parse_url)
        return response.json()["data"][0]
