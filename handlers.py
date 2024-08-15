import logging
from bingx_api import open_position, set_leverage

logger = logging.getLogger(__name__)

async def handle_new_message(event):
    message_text = event.message.message
    logger.info(f"Received message: {message_text}")

    if "buy" in message_text:
        response = open_position('BTCUSDT', 'buy')  # Замените 'BTCUSDT' на нужный символ
        await event.reply(f"Ответ от BingX: {response}")
    elif "sell" in message_text:
        response = open_position('BTCUSDT', 'sell')  # Замените 'BTCUSDT' на нужный символ
        await event.reply(f"Ответ от BingX: {response}")
    else:
        await event.reply("Неизвестная команда.")
