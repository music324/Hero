from os import getenv
import os
from dotenv import load_dotenv

# For Local Deploy
if os.path.exists("Internal"):
    load_dotenv("Internal")

# VARS

get_queue = {}
BOT_TOKEN = getenv("BOT_TOKEN", "5834312062:AAGgwcjbP5bkphbyeKeIgBkdHJhJrsaW4co")
API_ID = int(getenv("API_ID", "19275563"))
API_HASH = getenv("API_HASH", "332213ccd9f10bd2924e4824172e791e")
DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", "900"))
MONGO_DB_URI = getenv("MONGO_DB_URI", "")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5908792351").split()))
OWNER_ID = list(map(int, getenv("OWNER_ID", "5908792351").split()))
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", "-1001862187178"))
MUSIC_BOT_NAME = getenv("MUSIC_BOT_NAME", "-●⏤͟͟͞͞ ꜱᴘᴏᴛɪꜰʏ ✗ ᴍᴜsɪᴄ🕊️⃝🫧")
HEROKU_API_KEY = getenv("HEROKU_API_KEY")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO", "https://github.com/Venom-xd-89/Hero"
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")

if str(getenv("SUPPORT_CHANNEL")).strip() == "https://t.me/StarbotUpdate":
    SUPPORT_CHANNEL = None
else:
    SUPPORT_CHANNEL = str(getenv("SUPPORT_CHANNEL"))
if str(getenv("SUPPORT_GROUP")).strip() == "":
    SUPPORT_GROUP = None
else:
    SUPPORT_GROUP = str(getenv("SUPPORT_GROUP", "https://t.me/Super_Star_Singing_Group"))


if str(getenv("STRING_SESSION1")).strip() == "":
    STRING1 = str(None)
else:
    STRING1 = str(getenv("STRING_SESSION1"))

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
    LOG_SESSION = str(getenv("LOG_SESSION"))
