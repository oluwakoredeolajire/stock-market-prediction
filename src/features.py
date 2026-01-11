from src.config import TARGET_COLUMN

def create_moving_average(data, window_size):
    "Calculates the moving average for a given window size."
    for window in window_size:
        data[f'MA_{window}'] = data[TARGET_COLUMN].rolling(window=window).mean()
    return data
