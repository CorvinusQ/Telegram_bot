import logging
from telethon import TelegramClient
from dotenv import load_dotenv
import os
from handlers import handle_new_message

# Загрузка переменных окружения
load_dotenv()

# Настройки Telethon
api_id = os.getenv('TELEGRAM_API_ID')
api_hash = os.getenv('TELEGRAM_API_HASH')

# Настройка логирования
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

client = TelegramClient('session_name', api_id, api_hash)

@client.on(events.NewMessage)
async def new_message_event(event):
    await handle_new_message(event)

# Запуск клиента
with client:
    client.run_until_disconnected()
