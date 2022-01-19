import logging
from aiogram import Bot, Dispatcher, executor, types
from auth_data import TOKEN 
from aiogram.dispatcher.filters import Text
from aiogram.utils.markdown import hbold, link
from functionality import collect_data
import time

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands="start")
async def start(message: types.Message):
    start_buttons = ['Фалеристика СССР']
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*start_buttons)

    await message.answer('Выберите категорию', reply_markup=keyboard)


@dp.message_handler(Text(equals="Фалеристика СССР"))
async def get_discount_faleristics_SSSR(message: types.Message):
    await message.answer("Please waiting...")

    collect_data()

    with open("all_lots.txt", "r", encoding="utf-8") as file:
        index = 0
        while True:
            line = file.readline()
            if not line:
                break
            a, b = line.split(" -- ")
            card = f"{link(a, b)}"
            index += 1
            if index % 20 == 0:
                time.sleep(3)

            await message.answer(card)


def main():
    executor.start_polling(dp, skip_updates=True)


if __name__ == "__main__":
    main()
