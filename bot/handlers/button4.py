from aiogram.types import CallbackQuery

from api_services import GS_CLIENT


# функция для обработки коллбэка для получения значения колонки А2 из таблички TASTYTEST
async def get_a2_worksheet_val_query_handler(cb: CallbackQuery):
    # Шлём спиннер, тк запросы к таблицам всегда убогость долгая
    spinner = await cb.message.answer("💬")
    # Получаем значение ячейки (мы в коллбэк дата зашили "А2")
    val = GS_CLIENT.open("TASTYTEST").sheet1.acell(cb.data).value
    # удаляем спиннер
    await spinner.delete()
    # возвращаем ответ пользователю
    await cb.message.answer(f"Значение ячейки А2: {val}")