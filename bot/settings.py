from os import getenv


# Если мы не в докере - загружаем .env
DOCKER = getenv("DOCKER", "0") == "1"
if not DOCKER:
    from dotenv import load_dotenv
    load_dotenv()


# Токен у @BotFather
BOT_TOKEN = getenv("BOT_TOKEN")
# ЗАГУГЛИ как получить
GOOGLE_CREDS_FILENAME = getenv("GOOGLE_CREDS_FILENAME")
# Ресурсы на которых искать табличку (гугл поможет какие выбрать)
GOOGLE_SCOPES = ["https://www.googleapis.com/auth/spreadsheets", ]
# Имя таблички
GOOGLE_SHEET_NAME = getenv("TASYTEST")
# У @BotFather в настройках бота -> payments , там разберёшься
SBER_TOKEN = getenv("SBER_TOKEN")

# Котоссылка
CAT_URL = "https://cataas.com/cat"
