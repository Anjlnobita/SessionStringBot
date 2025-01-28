import os
import re
import logging
import logging.config
from dotenv import load_dotenv

load_dotenv(override=True)

pattern = re.compile(r"^.\d+$")

# vars
APP_ID = 20650066
API_HASH = "7a4f8ed638f1369a40693574c2835217"

BOT_TOKEN = "7970949227:AAHHqi_yNrnpN4w0criBvVri_YX6D1BmUKg"
OWNER_ID = 6777860063
MUST_JOIN = os.environ.get("MUST_JOIN", "")
ADMINS = [
    int(user) if pattern.search(user) else user
    for user in os.environ.get("ADMINS", "").split()
] + [OWNER_ID]


# logging Conf
logging.config.fileConfig(fname='config.ini', disable_existing_loggers=False)
LOGGER = logging.getLogger(__name__)
logging.getLogger("pyrogram").setLevel(logging.WARNING)