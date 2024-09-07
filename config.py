#(©)CodeXBotz




import os
import logging
from logging.handlers import RotatingFileHandler



#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "5350587359:AAF7PU_1uXH_lfc6UKQ3Pbo6Zoe83_MEFJM")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "12858393"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "a295383aca802e9a3cd01df1fefe2310")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1001785260530"))

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "1067513987"))

#Port
PORT = os.environ.get("PORT", "8080")

#Database 
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://UI:UI@cluster0.zggdk.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
DB_NAME = os.environ.get("DATABASE_NAME", "filesharexbot")

#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1001931453107"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

#start message
START_MSG = os.environ.get("START_MESSAGE", "<b>Sᴏʀʀʏ ɪ ᴏɴʟʏ ᴡᴏʀᴋ ᴏɴ Cɪɴᴇᴍᴀᴄᴏᴍᴘᴀɴʏ Gʀᴏᴜᴘ. Nᴏ ᴏᴛʜᴇʀ ᴄᴏᴍᴍᴀɴᴅ ᴡɪʟʟ ᴡᴏʀᴋ ᴏɴ ᴛʜɪs ʙᴏᴛ ᴇxᴄᴇᴘᴛ sᴛᴀʀᴛ. ᴅᴏɴ’ᴛ ᴡᴀsᴛᴇ ʏᴏᴜʀ ᴛɪᴍᴇ</b>")
try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "Hello {first}\n\n<b>You need to join in my Channel/Group to use me\n\nKindly Please join Channel</b>")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", "False") == 'False'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "<b>ഞാൻ അഡ്മിൻ പറയുന്നത് മാത്രമേ അനുസരിക്കു.\n\n<spoiler>വല്ല പണിക്കും പോടോ</spoiler></b>"

ADMINS.append(OWNER_ID)
ADMINS.append(1250450587)

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
