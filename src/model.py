from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor

def train_linear_regression(X_train, y_train):
    "Trains a Linear Regression model."
    model = LinearRegression()
    model.fit(X_train, y_train)
    return model

def train_random_forest(X_train, y_train, n_estimators=100):
    "Trains a Random Forest Regressor model."
    model = RandomForestRegressor(n_estimators=n_estimators)
    model.fit(X_train, y_train)
    return model