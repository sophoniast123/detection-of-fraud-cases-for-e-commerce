import pandas as pd
from pathlib import Path

class DataLoader:
    def __init__(self):
        # Always resolve paths from project root
        self.project_root = Path(__file__).resolve().parent.parent
        self.raw_data_path = self.project_root / "data" / "raw"

    def load_fraud_data(self):
        return pd.read_csv(self.raw_data_path / "Fraud_Data.csv")

    def load_ip_country_data(self):
        return pd.read_csv(self.raw_data_path / "IpAddress_to_Country.csv")

    def load_creditcard_data(self):
        return pd.read_csv(self.raw_data_path / "creditcard.csv")
