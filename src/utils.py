import pandas as pd
import matplotlib.pyplot as plt

def plot_predictions(dates, actual, predicted, title="Actual vs Predicted Stock Prices"):
    "Plots actual vs predicted stock prices."
    dates = pd.to_datetime(dates)
    plt.figure(figsize=(12, 6))
    plt.plot(dates, actual, label='Actual Prices', color='blue')
    plt.plot(dates, predicted, label='Predicted Prices', color='red', linestyle='--')
    plt.xlabel('Date')
    plt.ylabel('Stock Price')
    plt.xticks(rotation=45, ha='right')
    plt.title(title)
    plt.legend()
    plt.tight_layout()
    plt.show()
    plt.close()