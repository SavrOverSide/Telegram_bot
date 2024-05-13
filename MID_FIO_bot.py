# 1. Импорт библиотек
import logging
import os
import asyncio

from aiogram import Bot, Dispatcher, types
from transliterate import translit, get_translit_function

from aiogram.types import Message # ловим все обновления этого типа
from aiogram.filters.command import Command # обрабатываем команды /start, /help и другие

# 2. Инициализация объектов

TOKEN = os.getenv('TOKEN')
bot = Bot(token=TOKEN)
dp = Dispatcher()
logging.basicConfig(level=logging.INFO)

# Словарь для транслитерации
translit_dict = {
    'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ё': 'e', 'ж': 'zh',
    'з': 'z', 'и': 'i', 'й': 'i', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o',
    'п': 'p', 'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'kh', 'ц': 'ts',
    'ч': 'ch', 'ш': 'sh', 'щ': 'shch', 'ъ': 'ie', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'iu',
    'я': 'ia', 'А': 'A', 'Б': 'B', 'В': 'V', 'Г': 'G', 'Д': 'D', 'Е': 'E', 'Ё': 'E',
    'Ж': 'Zh', 'З': 'Z', 'И': 'I', 'Й': 'I', 'К': 'K', 'Л': 'L', 'М': 'M', 'Н': 'N',
    'О': 'O', 'П': 'P', 'Р': 'R', 'С': 'S', 'Т': 'T', 'У': 'U', 'Ф': 'F', 'Х': 'Kh',
    'Ц': 'Ts', 'Ч': 'Ch', 'Ш': 'Sh', 'Щ': 'Shch', 'Ъ': 'Ie', 'Ы': 'Y', 'Ь': '', 'Э': 'E',
    'Ю': 'Iu', 'Я': 'Ia'
}

# 3. Обработка команды start
@dp.message(Command(commands=['start']))
async def send_welcome(message: Message):
    await message.reply("Введите ваше ФИО на кириллице.")

# 4. Перевод ФИО из кириллицы в латиницу

@dp.message()
async def translate_fio(message: Message):
    fio = message.text
    latin_fio = ''.join(translit_dict.get(c, c) for c in fio)
    await message.reply(f"Ваше ФИО на латинице: {latin_fio}")

# 5. Запуск процесса пуллинга
if __name__ == '__main__':
    dp.run_polling(bot)
