import pandas as pd

def load_data(filepath):
    "Loads data from a CSV file into a pandas DataFrame."
    return pd.read_csv(filepath)
