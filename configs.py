# (c) @AbirHasan2005

import os
import logging

logging.basicConfig(
    format='%(name)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler('log.txt'),
              logging.StreamHandler()],
    level=logging.INFO
)


class Config(object):
    API_ID = int(os.environ.get("API_ID", "23562768"))
    API_HASH = os.environ.get("API_HASH", "1b40c01ae078463626e1b4e8fe78e3a5")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6323432432:AAHs9kG2qQdx2Y3LzSDqJwAdZEd39R9hOTQ")
    DOWNLOAD_DIR = os.environ.get("DOWNLOAD_DIR", "./downloads")
    LOGGER = logging
    OWNER_ID = int(os.environ.get("OWNER_ID", 1078225192))
    PRO_USERS = list(set(int(x) for x in os.environ.get("PRO_USERS", "0").split()))
    PRO_USERS.append(1078225192)
    MONGODB_URI = os.environ.get("MONGODB_URI", "mongodb+srv://mongodb091:mL5von9HmS6lDleu@cluster0.zavutq0.mongodb.net/?retryWrites=true&w=majority")
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001878894820"))
    BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", "False"))
