from aiogram import Bot
from aiogram.types import CallbackQuery, LabeledPrice, PreCheckoutQuery, Message
from settings import SBER_TOKEN


# функция для обработки коллбэка на оплату 2 рублёв
async def want_to_pay10rub_query_handler(cb: CallbackQuery):
    # посылаем инвойс на оплату
    await cb.message.answer_invoice(
        title="Просто так отдать 10 рублей (с тестовой карты конечно)",  # заголовок сообщения
        description=f"Тестовая карта: 6390 0200 0000 000003 (больше цифр, не ошибка), 12/24, CVC 123, код 12345678",  # содержание
        provider_token=SBER_TOKEN,  # токен юкассы
        payload=f"{cb.from_user.id}",  # пейлоад с id юзера
        currency="rub",  # валюта
        prices=[  # ценник
            LabeledPrice(
                label="10\u20DB",
                amount=10 * 100
            ),
        ],
        start_parameter="Assist_bot",  # рандомная дичь, я обычно тут ник бота пишу
        provider_data=None,  # данные провайдера
        need_name=False,  # нужно ли клиенту указывать имя
        need_phone_number=False,  # ^^^ телефон
        need_email=False,  # ^^^ мыло
        need_shipping_address=False,  # адрес если мы что-то доставляем
        is_flexible=False,  # может ли измениться цена (скидки и т.п.)
        disable_notification=False,  # не уведомлять об успешном платеже
        protect_content=False,  # защитить сообщение от пересылки
        reply_to_message_id=False,  # устаревший параметр
        request_timeout=60,  # таймаут для ожидания от юкассы
    )


# функция для ответа на пре-чекаут (телеграм его посылает чтобы убедиться, что бот на пол-пути не сломался)
async def process_pre_checkout_value(pre_checkout_query: PreCheckoutQuery, bot: Bot):
    # отвечаем, что бот в порядке и готов грести бабло
    await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)


# обработка успешного платежа
async def success_payment_handler(message: Message, bot: Bot):
    # получаем id пользователя из пейлоада
    user_id = message.successful_payment.invoice_payload
    # посылаем ответ. только через id, т.к. сообщение нам приходит от юкассы
    await bot.send_message(user_id, "Спс за 2 грамма кофе")
