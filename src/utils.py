import matplotlib.pyplot as plt

def plot_predictions(dates, actual, predicted):
    "Plots actual vs predicted stock prices."
    plt.figure(figsize=(10, 5))
    plt.plot(dates, actual, label='Actual Prices', color='blue')
    plt.plot(dates, predicted, label='Predicted Prices', color='red', linestyle='--')
    plt.xlabel('Date')
    plt.ylabel('Stock Price')
    plt.title('Actual vs Predicted Stock Prices')
    plt.legend()
    plt.show()