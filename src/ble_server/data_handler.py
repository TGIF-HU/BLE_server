import polars as pl
from polars import DataFrame, Series
import yaml


class CompanyID:
    def __init__(self, yaml_file: str):
        with open(yaml_file, "rb") as f:
            self.comp_data = yaml.safe_load(f)

    def get_Company(self, config: [int]) -> Series:
        # TODO
        return


def filter_duplicates(df: DataFrame) -> DataFrame:
    """
    重複している要素を削除する
    """
    # print(df)
    # TODO: 規格では時間の逆順になっているが、あまり信用できない
    return df.unique("MAC_ADDRESS", keep="last")
