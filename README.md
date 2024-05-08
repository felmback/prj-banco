# Notificação da cotação atual

## 📒 Descrição
Terá que informar a cotação atual de ações listada na B3

## 🤖 Tecnologias Utilizadas
Essencialmente, estamos construindo e treinando um modelo LSTM para prever preços futuros com base em dados históricos de preços de ações.

## 🧐 Processo de Criação
Começamos trazendo as ferramentas necessárias, como TensorFlow para criar modelos de aprendizado de máquina e NumPy para manipular dados em formato de array.
Script para recomendar a compra ou não de uma ação com base nas previsões, vamos introduzir um critério simples. 
Se o preço previsto for maior que o preço atual, sugerimos comprar; caso contrário, sugerimos não comprar. Além disso, para obter dados reais, podemos usar uma API financeira, como a Alpha Vantage, que fornece dados de mercado em tempo real.

## 🚀 Resultados
Papel: OIBR3
Preço atual: 0.72
Preço futuro: [0.5111191]
Recomendação: Não comprar
