import pandas as pd
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
import numpy as np
from tensorflow.keras.losses import MeanSquaredError


def train_model(data_file):
    df = pd.read_csv(data_file)
    X, y = [], []
    lookback = 60

    for i in range(len(df) - lookback):
        X.append(df[["close"]].iloc[i : i + lookback].values)
        y.append(df[["close"]].iloc[i + lookback].values)

    X, y = np.array(X), np.array(y)
    model = Sequential(
        [LSTM(50, return_sequences=True, input_shape=(lookback, 1)), LSTM(50), Dense(1)]
    )
    model.compile(optimizer="adam", loss=MeanSquaredError(), metrics=["accuracy"])

    model.fit(X, y, epochs=10, batch_size=32)
    model.save("models/price_predictor.h5")
    print("Model saved to models/price_predictor.h5")
