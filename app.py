# app.py

from flask import Flask, jsonify
import pandas as pd
from service_logic import get_recommendations, get_personalized_services

app = Flask(__name__)

# Load datasets
users = pd.read_csv('data/users.csv')
interactions = pd.read_csv('data/interactions.csv')
shoes = pd.read_csv('data/shoes.csv')
weather = pd.read_csv('data/weather.csv')

@app.route('/recommendations/<user_id>', methods=['GET'])
def recommend(user_id):
    try:
        recs = get_recommendations(user_id, users, interactions, shoes)
        return jsonify({'user_id': user_id, 'recommendations': recs})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/alerts/<user_id>', methods=['GET'])
def alerts(user_id):
    try:
        alerts = get_personalized_services(user_id, users, interactions, shoes, weather)
        return jsonify({'user_id': user_id, 'alerts': alerts})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
