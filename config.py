import os

TRADE_CONFIG = {
    'BTCUSDT': {
        'position_size': 0.01,
        'leverage': 10
    },
    'ETHUSDT': {
        'position_size': 0.1,
        'leverage': 10
    },
    'default': {
        'position_size': 0.01,
        'leverage': 10
    }
}

API_KEY = os.getenv('BINGX_API_KEY')
SECRET_KEY = os.getenv('BINGX_SECRET_KEY')
