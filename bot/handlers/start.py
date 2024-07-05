from aiogram.types import Message, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


# функция для ответа на команду /start
async def start_command_handler(message: Message):
    # строим клавиатуру
    builder = InlineKeyboardBuilder()
    builder.row(InlineKeyboardButton(text="КНОПКА АДИН. Г̶У̶Г̶Л̶ Яндекс-карта", callback_data="Москва, Ленина 1"))
    builder.row(InlineKeyboardButton(text="КНОПКА ДЫВА. Дай 2 рубля", callback_data="БАБЛО"))
    builder.row(InlineKeyboardButton(text="КНОПКА ТЫРИ. Получить котика", callback_data="КОТИК!"))
    builder.row(InlineKeyboardButton(text="КНОПКА ЧИТЫРИ. Узнать чо там на A2", callback_data="A2"))
    # шлём ответ на привет
    await message.answer(
        "Вот кнопки, а ещё можешь прислать мне дату, я её запишу.", reply_markup=builder.as_markup()
    )
