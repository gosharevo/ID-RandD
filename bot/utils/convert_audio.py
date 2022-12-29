"""
Модуль конвертации аудио сообщений в формат .wav 16кГц
"""

import os
import subprocess


async def convert_to_wav(filepath: str) -> str:
    new_filepath = os.path.splitext(filepath)[0] + '.wav'
    subprocess.call(['ffmpeg', '-i', filepath, '-acodec',
                     'pcm_s16le', '-ac', '1', '-ar', '16000', new_filepath],
                    stdout=subprocess.DEVNULL,
                    stderr=subprocess.STDOUT)

    return new_filepath
