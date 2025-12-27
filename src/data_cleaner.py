import pandas as pd

class DataCleaner:
    def remove_duplicates(self, df: pd.DataFrame) -> pd.DataFrame:
        return df.drop_duplicates()

    def handle_missing_values(self, df: pd.DataFrame) -> pd.DataFrame:
        # For this dataset, dropping missing rows is acceptable
        return df.dropna()

    def correct_dtypes(self, df: pd.DataFrame) -> pd.DataFrame:
        if "signup_time" in df.columns:
            df["signup_time"] = pd.to_datetime(df["signup_time"])
            df["purchase_time"] = pd.to_datetime(df["purchase_time"])
        return df
