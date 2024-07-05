import asyncio

from constructor_polling import main, test_bot, test_dp

# Классика
if __name__ == "__main__":
    # запускаемся. Обычно тут логгер логуру, но будет просто принт
    print("Стартуем")
    asyncio.new_event_loop().run_until_complete(main(test_bot, test_dp))
    print("Тухнем")
