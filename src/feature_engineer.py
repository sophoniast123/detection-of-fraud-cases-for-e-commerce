import pandas as pd

class FeatureEngineer:
    def add_time_features(self, df: pd.DataFrame) -> pd.DataFrame:
        # Ensure datetime columns are in proper dtype
        df["purchase_time"] = pd.to_datetime(df["purchase_time"])
        df["signup_time"] = pd.to_datetime(df["signup_time"])
        
        df["hour_of_day"] = df["purchase_time"].dt.hour
        df["day_of_week"] = df["purchase_time"].dt.dayofweek
        df["time_since_signup"] = (
            df["purchase_time"] - df["signup_time"]
        ).dt.total_seconds()
        return df

    def transaction_velocity(self, df: pd.DataFrame) -> pd.DataFrame:
        df = df.sort_values(["user_id", "purchase_time"]).copy()
        
        # Compute difference in seconds per user (vectorized)
        df["txn_diff_sec"] = df.groupby("user_id")["purchase_time"].diff().dt.total_seconds()
        
        # Flag transactions within 24 hours (86400 seconds)
        df["txn_count_24h"] = (df["txn_diff_sec"] < 86400).astype(int)
        
        # First transaction per user has NaN; fill with 0
        df["txn_count_24h"].fillna(0, inplace=True)
        
        # Optional: drop helper column
        df.drop(columns=["txn_diff_sec"], inplace=True)
        
        return df
