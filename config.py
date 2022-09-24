from os import getenv

from dotenv import load_dotenv

load_dotenv()

# VARS

get_queue = {}
BOT_TOKEN = getenv("BOT_TOKEN", "5687512550:AAGOkMv09dhcYMNC2kEZ75AUjPWG6QCLq_4")
API_ID = int(getenv("API_ID", "19837893"))
API_HASH = getenv("API_HASH", "8575adab8c4f5adf44c436f6c9ede458")
DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", "10"))
ASSISTANT_PREFIX = list(getenv("ASSISTANT_PREFIX", "/").split())
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://karatoz:049rpxQkwQhEu5fq@cluster0.ssoxpak.mongodb.net/?retryWrites=true&w=majority")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1990566455").split()))
OWNER_ID = list(map(int, getenv("OWNER_ID", "1990566455").split()))
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", "-1001652394597"))
MUSIC_BOT_NAME = getenv("MUSIC_BOT_NAME", "karatozmusic)
HEROKU_API_KEY = getenv("HEROKU_API_KEY", "4c823763-6593-4af7-8afd-69ad01588599")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME", "karatozbotmusic")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO", "https://github.com/AyiinXd/MultiAssistant"
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")

if str(getenv("SUPPORT_CHANNEL")).strip() == "":
    SUPPORT_CHANNEL = None
else:
    SUPPORT_CHANNEL = str(getenv("SUPPORT_CHANNEL"))
if str(getenv("SUPPORT_GROUP")).strip() == "":
    SUPPORT_GROUP = None
else:
    SUPPORT_GROUP = str(getenv("SUPPORT_GROUP"))


if str(getenv("STRING_SESSION1")).strip() == "":
    STRING1 = str(None)
else:
    STRING1 = str(getenv("STRING_SESSION1", "BQAshAU4ILmnh-yV2_FX13QrFtC4w8PXK15TYerDAsGyzUWs59kQJxMsMnHhHQSs4nIzXQiHbqstgKe_i16sttH7iD_JoTAlkm1FA3DvpEfvj_dwlqRZ6rBmf-jxtI5iJqZmp9McG3EuykHGiJ3aTEW1kvDUun1Jdfb0MZ6NHA2tnJMizs7UXXUhjqcJMmzZw9GPCpK3sDUES2uEyGKu_thiOlWEgUdowAjLmqpnKm8JaGqdgOWVsQGHqEsFfDohWYsoPerdic8jjPJnwumg_0d7J9WW1HpDL5yUI017YSqucDLMf8zDT_nnP7azDUtO7xPw6dEWw321zYSaW0wf1EqydqWiNwA"))

if str(getenv("STRING_SESSION2")).strip() == "":
    STRING2 = str(None)
else:
    STRING2 = str(getenv("STRING_SESSION2"))

if str(getenv("STRING_SESSION3")).strip() == "":
    STRING3 = str(None)
else:
    STRING3 = str(getenv("STRING_SESSION3"))

if str(getenv("STRING_SESSION4")).strip() == "":
    STRING4 = str(None)
else:
    STRING4 = str(getenv("STRING_SESSION4"))

if str(getenv("STRING_SESSION5")).strip() == "":
    STRING5 = str(None)
else:
    STRING5 = str(getenv("STRING_SESSION5"))

if str(getenv("LOG_SESSION")).strip() == "":
    LOG_SESSION = str(None)
else:
    LOG_SESSION = str(getenv("LOG_SESSION", "BQAshAU4ILmnh-yV2_FX13QrFtC4w8PXK15TYerDAsGyzUWs59kQJxMsMnHhHQSs4nIzXQiHbqstgKe_i16sttH7iD_JoTAlkm1FA3DvpEfvj_dwlqRZ6rBmf-jxtI5iJqZmp9McG3EuykHGiJ3aTEW1kvDUun1Jdfb0MZ6NHA2tnJMizs7UXXUhjqcJMmzZw9GPCpK3sDUES2uEyGKu_thiOlWEgUdowAjLmqpnKm8JaGqdgOWVsQGHqEsFfDohWYsoPerdic8jjPJnwumg_0d7J9WW1HpDL5yUI017YSqucDLMf8zDT_nnP7azDUtO7xPw6dEWw321zYSaW0wf1EqydqWiNwA"))
