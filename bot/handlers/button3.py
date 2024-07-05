from io import BytesIO

from aiogram.types import CallbackQuery, BufferedInputFile
from aiohttp import ClientSession

from settings import CAT_URL


# Функция для обработки коллбэка на запрос картинки
async def cat_image_query_handler(cb: CallbackQuery):
    # открываем котика
    async with ClientSession() as session:
        async with session.get(CAT_URL) as resp:
            b_cat = await resp.read()
            buf_file = BufferedInputFile(b_cat, "cat.jpeg")
    # шлём буфер с котиком и припиской
    await cb.message.answer_photo(buf_file, caption="Котик!")
