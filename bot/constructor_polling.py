from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.methods import DeleteWebhook
from settings import BOT_TOKEN
from handlers import (
    start_command_handler,
    yandex_maps_query_handler,
    want_to_pay10rub_query_handler,
    process_pre_checkout_value,
    success_payment_handler,
    cat_image_query_handler,
    get_a2_worksheet_val_query_handler,
    date_validate_handler,
)

# Создаём бота и диспетчер (для теста мне лень nginx + ssl на вебхуки поднимать)
test_bot = Bot(token=BOT_TOKEN)
test_dp = Dispatcher()

# Регистрируем ручки

# Команды
test_dp.message.register(start_command_handler, CommandStart())

# Коллбэки
test_dp.callback_query.register(yandex_maps_query_handler, F.data.startswith("Москва"))
test_dp.callback_query.register(want_to_pay10rub_query_handler, F.data == "БАБЛО")
test_dp.callback_query.register(cat_image_query_handler, F.data == "КОТИК!")
test_dp.callback_query.register(get_a2_worksheet_val_query_handler, F.data == "A2")

# Платёж
test_dp.pre_checkout_query.register(process_pre_checkout_value)
test_dp.message.register(success_payment_handler, F.successful_payment)

# Датавалидата
test_dp.message.register(date_validate_handler)


# Наше всё
async def main(bot: Bot, dispatcher: Dispatcher):
    # Пропускаем апдейты
    await bot(DeleteWebhook(drop_pending_updates=True))
    # Начинаем трясти телегу на предмет апдейтов
    await dispatcher.start_polling(bot, polling_timeout=10)