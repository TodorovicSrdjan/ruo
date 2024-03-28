import sys
import pandas as pd
import numpy as np
 
from sklearn.preprocessing import StandardScaler


def log_transform(col):
    return np.log(col[0])


def main():
    data = pd.read_csv(sys.argv[1])

    X = data.iloc[:,0:13]
    Y = data.iloc[:,13]

    scaler = StandardScaler()
    X = scaler.fit_transform(X)

    data["DIS"] = data[["DIS"]].apply(log_transform, axis=1)

    data.fillna(data.mean(), inplace=True)

    data.to_csv('cleaned.csv', index=False)

if __name__ == "__main__":
    main()