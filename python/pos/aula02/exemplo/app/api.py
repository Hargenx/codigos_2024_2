# app/api.py
from flask import Flask, jsonify
from data_loader import DataLoader
from analysis import Analysis

app = Flask(__name__)

# Carregar e pré-processar os dados
data_loader = DataLoader('titanic.csv')
data = data_loader.load_data()
data_loader.preprocess_data()
analysis = Analysis(data)

@app.route('/api/survival_rate', methods=['GET'])
def survival_rate():
    rate = analysis.survival_rate()
    return jsonify({"survival_rate": rate})

@app.route('/api/passenger/<int:id>', methods=['GET'])
def passenger(id):
    passenger_data = data.loc[data['PassengerId'] == id].to_dict(orient='records')
    return jsonify(passenger_data)

if __name__ == '__main__':
    app.run(debug=True)
