import os

TOKEN = os.getenv("BOT_TOKEN", "SIZNING_TOKENINGIZ")
ADMIN_IDS = [int(i) for i in os.getenv("ADMIN_IDS", "123456789").split(",")]
