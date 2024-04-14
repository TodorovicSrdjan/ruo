import sys
import pandas as pd
import numpy as np
import xgboost as xgb 

from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.metrics import precision_recall_fscore_support as score


def main():
    data = pd.read_csv(sys.argv[1])
    test_size = 1 - float(sys.argv[2])
    target_col = sys.argv[3]

    X = data.drop(target_col, axis=1)
    Y = data[target_col]
    
    X_train, X_test, Y_train, Y_test = train_test_split(
        X, Y, test_size=test_size, random_state=94)

    xgbr = xgb.XGBRegressor(objective='reg:squarederror')  #Our XGBoost model

    xgbr.fit(X_train, Y_train)

    #Generate predicted values
    Y_pred = xgbr.predict(X_test)

    #Calculate and print the RMSE and the accuracy of our model.
    mse = mean_squared_error(Y_test, Y_pred)
    score = r2_score(Y_test, Y_pred)

    rmse = "Root Mean Square Error: %.2f" % (mse**(0.5))
    acc = "Accuracy: {} %".format(round((score*100),2))

    print(rmse, acc, sep='\n')
    

if __name__ == "__main__":
    main()