from scripts.fetch_data import fetch_historical_data
from scripts.preprocess_data import preprocess_data
from scripts.predictor import train_model
from scripts.backtest import backtest

if __name__ == "__main__":
    # Fetch historical data
    fetch_historical_data("BTCUSDT", "1h", "1 Jan 2021")

    # Preprocess data
    preprocess_data("data/historical_data.csv")

    # Train model
    train_model("data/preprocessed_data.csv")

    # Backtest model
    backtest("models/price_predictor.h5", "data/historical_data.csv")
