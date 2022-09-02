import logging
from aiogram import Bot, Dispatcher, executor, types
import schedule_generate
import os

API_TOKEN = '5782093147:AAHFdL0qs6eSDYuAgFQ9ZR_JQYFRj2SQKUE'

logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.answer(f"я заебался чекать расписание вручную")

@dp.message_handler(commands=['расписание'])
async def schedule(message: types.Message):
    quantity = schedule_generate.get_screens()
    album = types.MediaGroup()
    for i in range(0, quantity):
        album.attach_photo(photo=types.InputFile(f'./screenshots/day{i}.png'))
    await message.answer_media_group(media=album)
    for i in range(0, quantity):
        os.remove(f'./screenshots/day{i}.png')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
