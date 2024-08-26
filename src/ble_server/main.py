import requests
from time import sleep
import json
import tomllib
import yaml
import polars as pl
from data_handler import filter_duplicates, CompanyID

threshold = 7


def get_ble_server(url: str) -> (int, pl.DataFrame):
    j = requests.get(url).json()
    ble_df = pl.DataFrame(j["ble"]).select(
        pl.col("address").alias("MAC_ADDRESS"),
        pl.col("rssi").alias("RSSI"),
        pl.col("manufacture_id").cast(pl.List(pl.UInt8)).alias("Company_ID"),
        pl.col("time").cast(pl.Datetime).alias("Time"),
    )
    device_id = j["device_id"]
    return device_id, ble_df


with open("config.toml", "rb") as f:
    ble_data = tomllib.load(f)

company_id = CompanyID("Company_ID_2024087.yaml")

while True:
    for device in ble_data["device"]:
        # デバイスの情報を取得
        device_id, ble_df = get_ble_server(device["url"])
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
