
# Stock Market Prediction Report

## Project Overview
This project aims to predict stock prices using historical data. It focuses on exploring, cleaning, and processing the stock market data, and applying machine learning models to forecast future stock prices. The following models were used for prediction:
- **Linear Regression**
- **Random Forest Regressor**


## Data Exploration
The dataset used in this project contains historical stock data with columns such as `Date`, `Open`, `High`, `Low`, `Close`, `Volume`, and `Adj Close`. The first step involved loading and cleaning the data, including handling missing values and converting the `Date` column to datetime format.

### Key Insights from Data Exploration:
- The closing price of stocks over time was visualized, showing patterns of volatility.
- Volume distribution was also explored, highlighting the frequency of different levels of trading activity.


## Data Preprocessing and Feature Engineering
In the preprocessing phase, we performed feature engineering to enhance the model's performance. Specifically, we created moving averages for 10-day and 50-day windows as additional features. These features were selected for their potential to smooth out short-term fluctuations and highlight longer-term trends in stock prices.

### Steps Taken:
1. Converted the `Date` column to datetime format.
2. Created moving average features.
3. Split the data into training and testing sets (80% train, 20% test).
4. Normalized the features using **MinMaxScaler**.


## Model Building

### Linear Regression:
- A simple linear regression model was trained to predict stock prices using the features.

### Random Forest Regressor:
- A Random Forest Regressor was trained, which is better at capturing complex patterns in the data.


## Model Evaluation

### Evaluation Metrics:
- **RMSE**: The Random Forest Regressor model had a slightly higher RMSE than Linear Regression, but both models performed similarly.
- **MAE**: Mean Absolute Error was calculated for both models, and Linear Regression showed slightly lower MAE than Random Forest Regressor.
- **R2 Score**: Both models achieved good R2 scores, indicating they explain a significant portion of the variance in stock prices.

### Feature Importance:
- The Random Forest Regressor model's feature importance was visualized, showing which features (e.g., `Volume`) had the most impact on the predictions. It identified 'Low' and 'High' price features as the most influential predictors in forecasting stock behavior. Specifically:
- Low Price had the highest relative importance, suggesting that the lowest trading price of the day carries strong predictive power for the target variable.
- High Price also contributed meaningfully, reinforcing the relevance of daily price range extremes in capturing market dynamics.
- MA_10 (10-day moving average), Volume, and Open Price showed no importance, indicating they did not influence predictive performance.


## Conclusion
The models performed well, with both Linear Regression and Random Forest showing promising results for stock price prediction. In this specific case, Linear Regression *slightly outperformed* Random Forest in terms of RMSE, despite Random Forest's ability to capture more complex, non-linear relationships in data. Linear Regression remains simpler and more interpretable.