"""
Основной модуль бота.
"""
from aiogram import executor

from bot import dp
from bot import commands
from bot import message_handlers

executor.start_polling(dp, skip_updates=True)
