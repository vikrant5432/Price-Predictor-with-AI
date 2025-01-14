import pandas as pd
from tensorflow.keras.models import load_model
import numpy as np


def backtest(model_file, data_file):
    df = pd.read_csv(data_file)
    model = load_model(model_file)
    lookback = 60
    X, y = [], []

    for i in range(len(df) - lookback):
        X.append(df[["close"]].iloc[i : i + lookback].values)
        y.append(df[["close"]].iloc[i + lookback].values)

    X, y = np.array(X), np.array(y)
    predictions = model.predict(X)

    predictions = predictions.flatten()
    y = y.flatten()

    accuracy = np.mean(np.round(predictions) == y)
    print(f"Backtest accuracy: {accuracy:.2%}")
