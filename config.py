import os
import logging
from logging.handlers import RotatingFileHandler




BOT_TOKEN = os.environ.get("BOT_TOKEN", "8176887548:AAELsQbL0CxdXlCuBm69WqbMA4XrSO3gOig")
API_ID = int(os.environ.get("API_ID", "979826"))
API_HASH = os.environ.get("API_HASH", "238183386c30590d073b457166ba260d")


OWNER_ID = int(os.environ.get("OWNER_ID", "1074804932"))
DB_URL = os.environ.get("DB_URL", "mongodb+srv://ygovcu:fY1f9Wovol3NqhUX@cluster0.1mdno.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = os.environ.get("DB_NAME", "Cluster0")


CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002358588449"))
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1001953560523"))


FILE_AUTO_DELETE = int(os.getenv("FILE_AUTO_DELETE", "900")) # auto delete in seconds


PORT = os.environ.get("PORT", "8080")
TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))



try:
    ADMINS=[6848088376]
    for x in (os.environ.get("ADMINS", "6848088376").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")









CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

DISABLE_CHANNEL_BUTTON = True if os.environ.get('DISABLE_CHANNEL_BUTTON', "True") == "True" else False

BOT_STATS_TEXT = "<b>BOT UPTIME :</b>\n{uptime}"







USER_REPLY_TEXT = "❌Don't Send Me Messages Directly I'm Only File Share Bot !"

START_MSG = os.environ.get("START_MESSAGE", "Hᴇʟʟᴏ {ᴍᴇɴᴛɪᴏɴ}\ɴ\ɴI Cᴀɴ Sᴛᴏʀᴇ Pʀɪᴠᴀᴛᴇ Fɪʟᴇs Iɴ Sᴘᴇᴄɪғɪᴇᴅ Cʜᴀɴɴᴇʟ Aɴᴅ Oᴛʜᴇʀ Usᴇʀs Cᴀɴ Aᴄᴄᴇss Iᴛ Fʀᴏᴍ Sᴘᴇᴄɪᴀʟ Lɪɴᴋ. ᴄʟɪᴄᴋ ʜᴇʀᴇ ᴛᴏ ᴄʜᴇᴄᴋ ᴛʜᴇ ᴘʀᴏᴄᴇᴅᴜʀᴇ @DᴇᴍᴏVɪᴅᴇᴏAɴɪᴍᴇ.")

FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "Hᴇʟʟᴏ {ᴍᴇɴᴛɪᴏɴ}\ɴ\ɴ<ʙ>Yᴏᴜ Nᴇᴇᴅ Tᴏ Jᴏɪɴ Iɴ Mʏ Cʜᴀɴɴᴇʟ/Gʀᴏᴜᴘ Tᴏ Usᴇ Mᴇ\ɴ\ɴKɪɴᴅʟʏ Pʟᴇᴀsᴇ Jᴏɪɴ Cʜᴀɴɴᴇʟ</ʙ>")





ADMINS.append(OWNER_ID)
ADMINS.append(6848088376)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
   





# Jishu Developer 
# Don't Remove Credit 🥺
# Telegram Channel @Madflix_Bots
# Backup Channel @JishuBotz
# Developer @JishuDeveloper
