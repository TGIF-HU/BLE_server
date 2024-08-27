import requests
import yaml
import polars as pl
from polars import DataFrame, Series


class CompanyID:
    def __init__(self, yaml_file: str):
        with open(yaml_file, "rb") as f:
            self.comp_data = yaml.safe_load(f)

    def get_Company(self, config: list[int]) -> Series:
        # TODO
        return


def get_ble_server(url: str) -> tuple[int, pl.DataFrame] | None:
    try:
        j = requests.get(url, timeout=(3.0, 7.5)).json()
    except requests.exceptions.RequestException as e:
        Warning("サーバーが見つかりませんでした")
        print(e)
        return None
    
    ble_df = pl.DataFrame(j["ble"]).select(
        pl.col("address").alias("MAC_ADDRESS"),
        pl.col("rssi").alias("RSSI"),
        pl.col("manufacture_id").cast(pl.List(pl.UInt8)).alias("Company_ID"),
        pl.col("time").cast(pl.Datetime).alias("Time"),
    )
    device_id = j["device_id"]
    return device_id, ble_df


def filter_duplicates(df: DataFrame) -> DataFrame:
    """
    重複している要素を削除する
    """
    # print(df)
    # TODO: 規格では時間の逆順になっているが、あまり信用できない
    return df.unique("MAC_ADDRESS", keep="last")
