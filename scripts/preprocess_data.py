import pandas as pd
from sklearn.preprocessing import MinMaxScaler


def preprocess_data(input_file):
    df = pd.read_csv(input_file)
    scaler = MinMaxScaler()
    df[["open", "high", "low", "close", "volume"]] = scaler.fit_transform(
        df[["open", "high", "low", "close", "volume"]]
    )
    df.to_csv("data/preprocessed_data.csv", index=False)
    print("Preprocessed data saved to data/preprocessed_data.csv")
