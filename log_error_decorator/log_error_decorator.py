import datetime
import os
import random

import requests
from dotenv import load_dotenv
from requests import Response

load_dotenv()


def get_random() -> str:
    arr = [f"http://api.marketstack.com/v1/eod?access_key={os.getenv('API_MARKETSTACK_KEY')}",
           f"http://api.marketstack.com/v1/eod/latest?access_key={os.getenv('API_MARKETSTACK_KEY')}&symbols=AAPL",
           f"http://api.marketstack.com/v1/eod/?symbols=AAPL",
           "http://api.marketstack.com/v5"]
    return random.choice(arr)


def log_error(func):
    def log_to_file(url: str):
        data = func(url)
        if data.status_code != 200 or data.elapsed.total_seconds() > 1:
            file = open(f"log_{datetime.datetime.now()}.txt", "w+")
            try:
                json = data.json()
                file.write(str(data.status_code))
                file.write(": ")
                file.write(json["error"]["message"])
            except KeyError as k:
                file.write("A long possibly successful response")

    return log_to_file


@log_error
def get_data_marketstack(url: str) -> Response:
    return requests.get(url)


get_data_marketstack(get_random())
