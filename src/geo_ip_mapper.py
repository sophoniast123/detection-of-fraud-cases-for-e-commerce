import pandas as pd
import numpy as np

class GeoIPMapper:
    def __init__(self, ip_df: pd.DataFrame):
        # Sort by lower bound IP for merge_asof
        self.ip_df = ip_df.copy()
        self.ip_df["lower_bound_ip_address"] = self.ip_df["lower_bound_ip_address"].astype(np.int64)
        self.ip_df["upper_bound_ip_address"] = self.ip_df["upper_bound_ip_address"].astype(np.int64)
        self.ip_df = self.ip_df.sort_values("lower_bound_ip_address")

    @staticmethod
    def ip_to_int(ip_series: pd.Series) -> pd.Series:
        return ip_series.astype(np.int64)

    def map_country(self, fraud_df: pd.DataFrame) -> pd.DataFrame:
        fraud_df = fraud_df.copy()
        fraud_df["ip_address"] = self.ip_to_int(fraud_df["ip_address"])

        # Use merge_asof for fast range matching
        fraud_df = fraud_df.sort_values("ip_address")
        merged = pd.merge_asof(
            fraud_df,
            self.ip_df,
            left_on="ip_address",
            right_on="lower_bound_ip_address",
            direction="backward"
        )

        # Keep only matches within upper bound
        merged["country"] = np.where(
            merged["ip_address"] <= merged["upper_bound_ip_address"],
            merged["country"],
            "Unknown"
        )

        return merged.drop(columns=["lower_bound_ip_address", "upper_bound_ip_address"])
