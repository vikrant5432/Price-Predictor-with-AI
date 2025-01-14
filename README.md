# Cryptocurrency Price Predictor

An AI-powered cryptocurrency price prediction system using deep learning and historical data from Binance.

## Overview

This project implements a cryptocurrency price prediction system using LSTM (Long Short-Term Memory) neural networks. The system fetches historical data from Binance, preprocesses it, trains a deep learning model, and provides backtesting capabilities to validate the model's performance.

## AI Approach

The project uses a Deep Learning approach with the following specifications:

- **Model Architecture**: Dual-layer LSTM (Long Short-Term Memory) neural network
- **Input Features**: 60-day historical price data (lookback period)
- **Output**: Next period price prediction
- **Layer Configuration**:
  - First LSTM Layer: 50 units with return sequences
  - Second LSTM Layer: 50 units
  - Dense Output Layer: 1 unit for price prediction

The LSTM architecture was chosen for its ability to:

- Capture long-term dependencies in time series data
- Handle sequential data effectively
- Learn patterns in price movements
- Remember important past information while forgetting irrelevant details

## Project Structure

```
project/
├── fetch_data.py      # Binance data collection
├── preprocess_data.py # Data normalization
├── predictor.py       # LSTM model training
├── backtest.py        # Model validation
├── data/             # Data storage
└── models/           # Trained models
```

## Components

### 1. Data Collection (fetch_data.py)

- Integrates with Binance API
- Fetches historical OHLCV data
- Saves raw data to CSV format

### 2. Data Preprocessing (preprocess_data.py)

- Normalizes OHLCV data using MinMaxScaler
- Prepares data for model training
- Handles missing values and outliers

### 3. Model Training (predictor.py)

- Implements LSTM neural network
- Configures model architecture
- Trains on historical data
- Saves trained model

### 4. Backtesting (backtest.py)

- Validates model performance
- Calculates prediction accuracy
- Tests against historical data

## Setup and Usage

1. Install dependencies:

```bash
pip install pandas numpy tensorflow sklearn python-binance
```

2. Fetch historical data:

```python
from fetch_data import fetch_historical_data
fetch_historical_data("BTCUSDT", "1h", "1 Jan 2023")
```

3. Preprocess the data:

```python
from preprocess_data import preprocess_data
preprocess_data("data/historical_data.csv")
```

4. Train the model:

```python
from predictor import train_model
train_model("data/preprocessed_data.csv")
```

5. Run backtesting:

```python
from backtest import backtest
backtest("models/price_predictor.h5", "data/preprocessed_data.csv")
```

## Future Improvements

1. Enhanced Feature Engineering:

   - Technical indicators (RSI, MACD, etc.)
   - Market sentiment analysis
   - Volume profile analysis

2. Model Enhancements:

   - Hyperparameter optimization
   - Cross-validation implementation
   - Ensemble methods

3. Backtesting Improvements:
   - Additional performance metrics
   - Risk analysis
   - Trading simulation

## License

[Your chosen license]

## Contributing

[Contributing guidelines]
