import yfinance as yf
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, LSTM, Dropout

# 1. Obter dados financeiros
ticker = "AAPL"  # Exemplo de ativo
data = yf.download(ticker, start="2015-01-01", end="2023-01-01")
data = data[["Adj Close", "Volume"]]  # Usar o preço ajustado e o volume

# 2. Criar a base de dados de preços e volume
data["Returns"] = data["Adj Close"].pct_change()
data.dropna(inplace=True)

# 3. Criar uma rede (neural)
scaler = MinMaxScaler(feature_range=(0, 1))
scaled_data = scaler.fit_transform(data)

X = []
y = []

for i in range(60, len(scaled_data)):
    X.append(scaled_data[i - 60 : i, 0])
    y.append(scaled_data[i, 0])

X, y = np.array(X), np.array(y)
X = np.reshape(X, (X.shape[0], X.shape[1], 1))

# 4. Construir o modelo LSTM
model = Sequential()

model.add(LSTM(units=50, return_sequences=True, input_shape=(X.shape[1], 1)))
model.add(Dropout(0.2))
model.add(LSTM(units=50, return_sequences=False))
model.add(Dropout(0.2))
model.add(Dense(units=25))
model.add(Dense(units=1))

model.compile(optimizer="adam", loss="mean_squared_error")

# 5. Treinar o modelo
model.fit(X, y, batch_size=1, epochs=1)

# 6. Simular o comportamento de um agente
# Aqui você pode implementar um agente simples que decide comprar ou vender com base nas previsões do modelo

# Prever os preços futuros
predictions = model.predict(X)

# Comparar previsões com preços reais
# (Aqui você precisa ajustar o código para avaliar a precisão do modelo)
