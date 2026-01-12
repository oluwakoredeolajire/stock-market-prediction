# Stock Market Prediction

## Problem Statement
The goal of this project is to predict stock prices based on historical data. Specifically, the project focuses on predicting the closing price of a given stock for a future time period using **Linear Regression** and **Random Forest Regressor** machine learning models. Stock price prediction is a critical task in finance, where investors and traders need to make informed decisions based on the historical trends and market data.

## Dataset Description
The dataset used in this project consists of historical stock market data for Atlantic American Corporation, and it contains the following columns:
1. Date: The date of the stock data.
2. Open: The price at which the stock opened on that day.
3. High: The highest price of the stock on that day.
4. Low: The lowest price of the stock on that day.
5. Close: The price of the stock at market close on that day (this is the target variable we aim to predict).
6. Volume: The number of shares traded during the day.
7. Adj Close: The adjusted closing price, taking into account corporate actions like stock splits and dividends.
The dataset spans a long period of time (1980-2020) and has daily frequency.

-----

## Overview
This project consists of the following main steps:
1. **Data Exploration:** Understanding the raw stock market data and visualizing key statistics.
2. **Data Preprocessing:** Cleaning the data, handling missing values, and feature engineering.
3. **Model Building:** Training Linear Regression and Random Forest Regressor machine learning models.
4. **Evaluation:** Assessing the performance of the models using various evaluation metrics and visualizing the results.

-----

## Setup
1. Clone the repository:
    - git clone https://github.com/oluwakoredeolajire/stock-market-prediction.git
    - cd stock-market-prediction

2. Create a virtual environment and activate it:
    - python3 -m venv env
    - env\Scripts\activate [On Windows]

3. Install dependencies:
    - pip install -r requirements.txt

-----

## Usage
To work with the notebooks, simply open them using Jupyter. Then, navigate to the notebooks folder and open each notebook (data_exploration.ipynb, data_preprocessing.ipynb, etc.) to explore the code.

-----

## Report
The project also includes a stock prediction report [Report](reports/stock_prediction_report.md), which provides an analysis of the data, model performance, and results.

-----

## License
This project is licensed under the MIT License. See the LICENSE file for details.