import pandas as pd
import os


class DAT:


    @staticmethod
    def load_csv():
        if not os.path.exists("data"):
            raise FileNotFoundError(f"Directory data does not exist.")

        files = os.listdir("data")
        if not files:
            raise FileNotFoundError(f"No files found in directory data.")

        filename = files[0]
        path = os.path.join("data", filename)

        try:
            df = pd.read_csv(path)
        except Exception as e:
            raise ValueError(f"Failed to read CSV: {e}")

        if df.empty:
            raise ValueError("Loaded CSV is empty.")

        return df