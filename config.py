import os

# Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "8449716285:AAF4_EiRd8LqUy1peJOfSJrUbV-AxE9tu9s")

# Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "12380656"))

# Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "d927c13beaaf5110f25c505b7c071273")

# Your Owner / Admin Id For Broadcast 
ADMINS = int(os.environ.get("ADMINS", "6123741920"))

# Your Mongodb Database Url
# Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_URI = os.environ.get("DB_URI", "mongodb+srv://pandubaby4:pandubaby4@cluster0.yexd02h.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0") # Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_NAME = os.environ.get("DB_NAME", "pandubaby4")

# If You Want Error Message In Your Personal Message Then Turn It True Else If You Don't Want Then Flase
ERROR_MESSAGE = bool(os.environ.get('ERROR_MESSAGE', True))
