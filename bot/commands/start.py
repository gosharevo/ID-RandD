"""
Модуль обработчика команды /start
"""
from aiogram import types

from .. import dp
from ..consts import messages as mc

MODULE_NAME = 'start'


@dp.message_handler(commands=[MODULE_NAME])
async def start(message: types.Message):
    """
    Функция обработки команды /start
    """
    await message.answer(text=mc.START_TEXT, parse_mode=types.ParseMode.HTML)
