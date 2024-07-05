from aiogram.types import Message
from dateparser import parse

from api_services import GS_CLIENT


# функция для обработки пользовательского сообщения с датой
async def date_validate_handler(message: Message):
    # парсим дату
    date = parse(message.text.lower())
    # если не нашли
    if not date:
        # ш̶л̶ё̶м̶ ̶п̶о̶л̶ь̶з̶о̶в̶а̶т̶е̶л̶я̶ любезно сообщаем пользователю, что он неправ
        await message.answer("Не могу понять дату. Введи, например, 'вчера' или '11.01.2024 18:00'")
        # тут всё
        return
    # получилось спарсить, сообщаем пользователю, что он молодец
    date = date.strftime("%d.%m.%Y")
    await message.answer(f"Дата норм, записал как {date}")
    # записывать будем в колонку B, а она вторая по счёту
    col = 2
    # открывем табличку
    wks = GS_CLIENT.open("TASTYTEST").sheet1
    # находим последнюю пустую строку в колонке 2(B)
    last_row = len(wks.col_values(2))
    # Пишем
    wks.update_cell(col=col, row=last_row+1, value=date)
