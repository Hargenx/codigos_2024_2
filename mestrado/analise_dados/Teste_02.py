"""
financial_analysis
Copyright (c) 2024 Raphael M. S. de Jesus
Release under the Windows 11
Python 3.12 - Jupyter notebook
Tested with 64 bit (AMD64) and 64 bit (Intel-I5)
"""

# Importação de bibliotecas necessárias
import yfinance as yf
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, LSTM, Dropout
from sklearn.metrics import mean_squared_error, mean_absolute_error
import matplotlib.pyplot as plt


def fetch_data(ticker: str, start_date: str, end_date: str) -> pd.DataFrame:
    """
    Função para obter dados financeiros históricos de um ativo.

    Args:
    - ticker (str): Símbolo do ativo.
    - start_date (str): Data de início no formato 'YYYY-MM-DD'.
    - end_date (str): Data de término no formato 'YYYY-MM-DD'.

    Returns:
    - data (pd.DataFrame): Dados financeiros históricos.
    """
    data = yf.download(ticker, start=start_date, end=end_date)
    data = data[["Adj Close", "Volume"]]  # Selecionar preço ajustado e volume
    return data


def preprocess_data(data: pd.DataFrame) -> tuple:
    """
    Função para processar dados financeiros, calcular retornos e normalizar.

    Args:
    - data (pd.DataFrame): Dados financeiros históricos.

    Returns:
    - X, y (np.ndarray): Matrizes de features e labels para treinamento.
    - scaler (MinMaxScaler): Objeto de normalização.
    """
    data["Returns"] = data["Adj Close"].pct_change()
    data.dropna(inplace=True)

    scaler = MinMaxScaler(feature_range=(0, 1))
    scaled_data = scaler.fit_transform(data)

    X, y = [], []
    for i in range(60, len(scaled_data)):
        X.append(scaled_data[i - 60 : i, 0])
        y.append(scaled_data[i, 0])

    X, y = np.array(X), np.array(y)
    X = np.reshape(X, (X.shape[0], X.shape[1], 1))

    return X, y, scaler


def build_lstm_model(input_shape: tuple) -> Sequential:
    """
    Função para construir o modelo LSTM.

    Args:
    - input_shape (tuple): Formato de entrada do modelo.

    Returns:
    - model (Sequential): Modelo LSTM compilado.
    """
    model = Sequential()
    model.add(LSTM(units=50, return_sequences=True, input_shape=input_shape))
    model.add(Dropout(0.2))
    model.add(LSTM(units=50, return_sequences=False))
    model.add(Dropout(0.2))
    model.add(Dense(units=25))
    model.add(Dense(units=1))
    model.compile(optimizer="adam", loss="mean_squared_error")
    return model


def simulate_trading(predictions: np.ndarray, data: pd.DataFrame, threshold=0.01) -> float:
    """
    Simular o comportamento de um agente de trading simples.

    Args:
    - predictions (np.ndarray): Previsões do modelo.
    - data (pd.DataFrame): Dados financeiros históricos.
    - threshold (float): Limiar de decisão de compra/venda.

    Returns:
    - final_portfolio_value (float): Valor final do portfólio do agente.
    """
    cash = 10000
    shares = 0
    transactions = []

    for i in range(1, len(predictions)):
        if predictions[i] > predictions[i - 1] * (1 + threshold):
            shares_to_buy = cash // data["Adj Close"].iloc[i]
            cash -= shares_to_buy * data["Adj Close"].iloc[i]
            shares += shares_to_buy
            transactions.append(("buy", i, data["Adj Close"].iloc[i]))
        elif predictions[i] < predictions[i - 1] * (1 - threshold):
            cash += shares * data["Adj Close"].iloc[i]
            transactions.append(("sell", i, data["Adj Close"].iloc[i]))
            shares = 0

    final_portfolio_value = cash + shares * data["Adj Close"].iloc[-1]
    return final_portfolio_value


def evaluate_model(predictions: np.ndarray, data: pd.DataFrame, scaler: MinMaxScaler) -> tuple:
    """
    Avaliar o modelo comparando previsões com preços reais.

    Args:
    - predictions (np.ndarray): Previsões do modelo.
    - data (pd.DataFrame): Dados financeiros históricos.
    - scaler (MinMaxScaler): Objeto de normalização.

    Returns:
    - mse, mae (float): Mean Squared Error e Mean Absolute Error.
    """
    scaled_predictions = scaler.inverse_transform(
        np.concatenate((predictions, np.zeros((len(predictions), 1))), axis=1)
    )[:, 0]
    mse = mean_squared_error(data["Adj Close"].iloc[60:], scaled_predictions)
    mae = mean_absolute_error(data["Adj Close"].iloc[60:], scaled_predictions)
    return mse, mae


def plot_predictions(data: pd.DataFrame, predictions: np.ndarray, scaler: MinMaxScaler) -> None:
    """
    Plotar previsões e preços reais para comparação.

    Args:
    - data (pd.DataFrame): Dados financeiros históricos.
    - predictions (np.ndarray): Previsões do modelo.
    - scaler (MinMaxScaler): Objeto de normalização.
    """
    scaled_predictions = scaler.inverse_transform(
        np.concatenate((predictions, np.zeros((len(predictions), 1))), axis=1)
    )[:, 0]
    plt.figure(figsize=(14, 5))
    plt.plot(data.index[60:], data["Adj Close"].iloc[60:], label="Preço Real")
    plt.plot(
        data.index[60:], scaled_predictions, label="Previsão do Modelo", linestyle="--"
    )
    plt.xlabel("Data")
    plt.ylabel("Preço Ajustado de Fechamento")
    plt.title("Comparação de Previsões de Preços")
    plt.legend()
    plt.show()


# Execução principal
if __name__ == "__main__":
    ticker = "AAPL"
    start_date = "2015-01-01"
    end_date = "2023-01-01"

    data = fetch_data(ticker, start_date, end_date)
    X, y, scaler = preprocess_data(data)
    model = build_lstm_model((X.shape[1], 1))
    model.fit(X, y, batch_size=1, epochs=1)

    predictions = model.predict(X)
    final_portfolio_value = simulate_trading(predictions, data)
    print(f"Valor final do portfólio: ${final_portfolio_value:.2f}")

    mse, mae = evaluate_model(predictions, data, scaler)
    print(f"Mean Squared Error (MSE): {mse:.4f}")
    print(f"Mean Absolute Error (MAE): {mae:.4f}")

    plot_predictions(data, predictions, scaler)
