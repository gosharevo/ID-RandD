"""
Модуль обработки аудио сообщений
"""
import os

from aiogram import types
from aiogram.types import ContentType

from .. import dp, bot
from ..config import base_config
from ..utils.convert_audio import convert_to_wav
from ..consts import messages as mc


@dp.message_handler(content_types=[ContentType.VOICE])
async def audio_message(message: types.Message):
    user_id = message.from_user.id

    voice_path = base_config.SAVE_PATH.format(user_id=user_id) + 'voice/'
    os.makedirs(voice_path, exist_ok=True)

    index = len(os.listdir(voice_path))

    voice_name = f'audio_message_{index}.ogg'
    save_path = os.path.join(voice_path, voice_name)

    await message.voice.download(destination_file=save_path)
    await convert_to_wav(save_path)

    os.remove(save_path)
    await bot.send_message(chat_id=user_id, text=mc.VOICE_SAVE_SUCCESS_TEXT)
