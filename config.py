#(©)t.me/CodeFlix_Bots




import os
import logging
from logging.handlers import RotatingFileHandler



#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "7518790192:AAFyeqJXVMRCJYIJ5SejzLuaspEWQgUFrkU")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "20170562"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "56aa61b4d1198329f24c1602eb3f73d4")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002052438967"))

# NAMA OWNER
OWNER = os.environ.get("OWNER", "GHOijsST")

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "7066319676"))

#Port
PORT = os.environ.get("PORT", "8018")

#Database
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://Backbenchersnevakakms:<PLs5YvLbUYWRJXk8>@cluster0.u3mmn.mongodb.net/")
DB_NAME = os.environ.get("DATABASE_NAME", "filesbyjbak")

#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1001559911506"))
FORCE_SUB_CHANNEL2 = int(os.environ.get("FORCE_SUB_CHANNEL2", "-1002044842213"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

#start message
START_MSG = os.environ.get("START_MESSAGE", "<b>Hello {first}</b>\n\nmuth marna band kr de dusro ko sex krte dekh muth marne maja aata kya?? cuck ho? eww bhai imagine tumhara brain itna fucked up ho chuka hai ki tum dusro ko sex krte dekh maja ata sad bhai ye sab band kr do @brainsaga if you want bot like this </a></b>")
try:
    ADMINS=[7066319676]
    for x in (os.environ.get("ADMINS", "7066319676").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "👋 Hello {first}!\nTo access these files you have to join our channel first.\nPlease subscribe to our channels through the buttons below and then tap on try again to get your files.\nThank You ❤️")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", "<b>By @brainsaga</a>")

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "ʙᴀᴋᴋᴀ ! ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴍʏ ꜱᴇɴᴘᴀɪ!!"

ADMINS.append(OWNER_ID)
ADMINS.append(7066319676)

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
   
