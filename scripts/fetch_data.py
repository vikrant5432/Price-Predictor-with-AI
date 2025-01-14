from binance.client import Client
import pandas as pd


def fetch_historical_data(symbol, interval, start_date):
    client = Client()
    klines = client.get_historical_klines(symbol, interval, start_date)
    df = pd.DataFrame(
        klines,
        columns=[
            "timestamp",
            "open",
            "high",
            "low",
            "close",
            "volume",
            "close_time",
            "quote_asset_volume",
            "number_of_trades",
            "taker_buy_base",
            "taker_buy_quote",
            "ignore",
        ],
    )
    df["timestamp"] = pd.to_datetime(df["timestamp"], unit="ms")
    df.to_csv("data/historical_data.csv", index=False)
    print("Historical data saved to data/historical_data.csv")
