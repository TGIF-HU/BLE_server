import requests
from time import sleep
import json
import tomllib
import yaml
import polars as pl
from data_handler import filter_duplicates, CompanyID, get_ble_server

threshold = 7


with open("config.toml", "rb") as f:
    ble_data = tomllib.load(f)

company_id = CompanyID("Company_ID_2024087.yaml")

while True:
    # TODO: 並列化
    for device in ble_data["device"]:
        # デバイスの情報を取得
        result = get_ble_server(device["url"])
        if result is None:
            continue
        else:
            device_id, ble_df = result
        print("---------------------------------------")
        print(f"Device ID: {device_id}")
        # print(ble_df)

        # データをフィルタリング
        ble_df = filter_duplicates(ble_df)  # TODO: 最新のデータのみをフィルタリングできている？
        print(ble_df)

        if len(ble_df) >= threshold:
            print("混雑しています")
        else:
            print("混雑していません")
    sleep(10)
