"""
Модуль обработки фото
"""
import os

from aiogram import types
from aiogram.types import ContentType

from .. import dp, bot
from ..config import base_config
from ..utils.serch_face import photo_faces
from ..consts import messages as mc


@dp.message_handler(content_types=[ContentType.PHOTO])
async def photo_message(message: types.Message):
    user_id = message.from_user.id

    photo_path = base_config.SAVE_PATH.format(user_id=user_id) + 'photo/'
    os.makedirs(photo_path, exist_ok=True)

    index = len(os.listdir(photo_path))
    message_photo = message.photo[-1]

    photo_name = f'photo_{index}.jpg'
    save_path = os.path.join(photo_path, photo_name)

    await message_photo.download(destination_file=save_path)

    if await photo_faces(save_path):
        await bot.send_message(chat_id=user_id, text=mc.PHOTO_SAVE_SUCCESS_TEXT)
    else:
        await bot.send_message(chat_id=user_id, text=mc.PHOTO_SAVE_FAILURE_TEXT)
        os.remove(save_path)
