import requests
from time import sleep
import tomllib

with open("config.toml", "rb") as f:
    data = tomllib.load(f)

while True:
    for device in data["device"]:
        r = requests.get(device["url"])
        print(r.json())
    sleep(10)