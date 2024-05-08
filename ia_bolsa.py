import numpy as np
import re
import requests
from bs4 import BeautifulSoup
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, LSTM


#script não pode ser usado para compras efetivamente , apenas para estudo e teste.
# Mas pode ser usado para previsão de ações futuras com algumas correções.

# Função para buscar o preço da ação no Google Finance
def get_stock_price(stock_symbol):
    url = f"https://www.google.com/finance/quote/{stock_symbol}:BVMF"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    price_string = soup.find("div", class_="YMlKec fxKbKc").text
    price = float(re.sub(r'[^\d.]', '', price_string))
    return price

# Gerar dados de exemplo (preços de ações)
def generate_data(n):
    # Vamos gerar preços de ações aleatórios para exemplo
    return np.random.rand(n)

# Preparar dados para treinamento
def prepare_data(data, n_steps):
    X, y = [], []
    for i in range(len(data)):
        end_ix = i + n_steps
        if end_ix > len(data)-1:
            break
        seq_x, seq_y = data[i:end_ix], data[end_ix]
        X.append(seq_x)
        y.append(seq_y)
    return np.array(X), np.array(y)

# Definir modelo LSTM
def create_model(n_steps, n_features):
    model = Sequential()
    model.add(LSTM(50, activation='relu', input_shape=(n_steps, n_features)))
    model.add(Dense(1))
    model.compile(optimizer='adam', loss='mse')
    return model

# Definir parâmetros
n_steps = 3
n_features = 1

# Gerar dados de exemplo
data = generate_data(100)

# Preparar dados para treinamento
X, y = prepare_data(data, n_steps)

# Redimensionar os dados para LSTM [amostras, etapas de tempo, características]
X = X.reshape((X.shape[0], X.shape[1], n_features))

# Criar e treinar o modelo
model = create_model(n_steps, n_features)
model.fit(X, y, epochs=100, verbose=0)

# Prever os próximos preços
def predict_next_prices(model, last_prices, n_steps, n_features):
    last_prices = np.array(last_prices)
    last_prices = last_prices.reshape((1, n_steps, n_features))
    next_price = model.predict(last_prices, verbose=0)
    return next_price[0]

# Exemplo de previsão para as próximas 3 etapas
stock_symbol = str(input("Digite o símbolo da ação: "))  # Símbolo da ação
value_initial = get_stock_price(stock_symbol)  # Obter o preço inicial da ação
last_prices = [value_initial for _ in range(n_steps)]  # Obter os preços mais recentes
next_prices = predict_next_prices(model, last_prices, n_steps, n_features)
print(f"Papel: {stock_symbol}\nPreço atual: {value_initial}\nPreço futuro: {next_prices}")
if next_prices > value_initial:
    print("Recomendação: Comprar")
else:
    print("Recomendação: Não comprar")