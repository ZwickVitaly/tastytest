from aiogram.enums import ParseMode
from aiogram.types import CallbackQuery


# Функция для обработки коллбэка на запрос яндекс-карт
async def yandex_maps_query_handler(cb: CallbackQuery):
    # получаем искомый адрес
    addr = cb.data
    # если адерс слишком длинный
    if len(addr) > 50:
        # обрезаем
        addr = addr[:50]
    # высылаем красивую ссылку
    await cb.message.answer(
        text=f'<a href="https://yandex.ru/maps/?mode=search&text={addr}">ЙАНДЕКСКАРТАА</a>', parse_mode=ParseMode.HTML
    )
