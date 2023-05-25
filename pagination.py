
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor



TOKEN = 'Telegram bot tokenni kiritish'


bot = Bot(token=TOKEN)
dp = Dispatcher(bot)



data = [
    'Item 1', 'Item 2', 'Item 3', 'Item 4', 'Item 5', 'Item 6', 'Item 7', 'Item 8', 'Item 9', 'Item 10',
    'Item 11', 'Item 12', 'Item 13', 'Item 14', 'Item 15', 'Item 16', 'Item 17', 'Item 18', 'Item 19', 'Item 20',
    'Item 21', 'Item 22', 'Item 23', 'Item 24', 'Item 25', 'Item 26', 'Item 27', 'Item 28', 'Item 29', 'Item 30',
    'Item 31', 'Item 32', 'Item 33', 'Item 34', 'Item 35', 'Item 36', 'Item 37', 'Item 38', 'Item 39', 'Item 40'
    ]


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await send_paginated_data(message.chat.id, 0)

@dp.callback_query_handler(lambda callback_query: True)
async def handle_pagination(callback_query: types.CallbackQuery):
    chat_id = callback_query.message.chat.id
    
    page = int(callback_query.data)

    await bot.delete_message(chat_id, callback_query.message.message_id)
    await send_paginated_data(chat_id, page)

async def send_paginated_data(chat_id: int, page: int):
    buttons = []
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    start_index = page * 10
    end_index = start_index + 10
    paginated_data = data[start_index:end_index]

    text = f"{page + 1} - Sahifa"
    for item in paginated_data:
        keyboard.insert(types.InlineKeyboardButton(item, callback_data='efwewef'))

    
    if page > 0:
        buttons.append(types.InlineKeyboardButton('Oldingi', callback_data=str(page - 1)))
    if end_index < len(data):
        buttons.append(types.InlineKeyboardButton('Keyingi', callback_data=str(page + 1)))

    keyboard.add(*buttons)

    await bot.send_message(chat_id, text, reply_markup=keyboard)



if __name__ == '__main__':
    executor.start_polling(dp)

