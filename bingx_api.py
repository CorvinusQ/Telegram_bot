import requests
import hmac
import hashlib
import time
from config import API_KEY, SECRET_KEY, TRADE_CONFIG


def generate_signature(payload):
    query_string = '&'.join([f"{key}={payload[key]}" for key in sorted(payload.keys())])
    return hmac.new(SECRET_KEY.encode('utf-8'), query_string.encode('utf-8'), hashlib.sha256).hexdigest()


def set_leverage(symbol, leverage):
    url = 'https://api.bingx.com/v1/leverage/set'
    payload = {
        'symbol': symbol,
        'leverage': leverage,
        'api_key': API_KEY,
        'timestamp': int(time.time() * 1000)
    }
    payload['signature'] = generate_signature(payload)

    response = requests.post(url, json=payload)
    return response.json()


def open_position(symbol, side):
    url = 'https://api.bingx.com/v1/order/place'
    timestamp = int(time.time() * 1000)

    config = TRADE_CONFIG.get(symbol, TRADE_CONFIG['default'])
    position_size = config['position_size']
    leverage = config['leverage']

    # Устанавливаем плечо перед открытием позиции
    set_leverage(symbol, leverage)

    payload = {
        'symbol': symbol,
        'side': side,
        'type': 'market',
        'quantity': position_size,
        'timestamp': timestamp,
        'api_key': API_KEY
    }

    payload['signature'] = generate_signature(payload)

    response = requests.post(url, json=payload)
    return response.json()
