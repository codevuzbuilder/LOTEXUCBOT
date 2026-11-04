import os

# GitHub Secrets dan oladi, agar localda bo'lsa env dan oladi
BOT_TOKEN = os.getenv("BOT_TOKEN")

# Agar env bo'sh bo'lsa, shu yerga qo'lda yoz (faqat local uchun)
if not BOT_TOKEN or "***" in BOT_TOKEN or len(BOT_TOKEN) < 20:
    BOT_TOKEN = "1234567890:AAH_YOUR_REAL_TOKEN_HERE"  # <-- BotFather dan olgan tokeningni yoz

ADMIN_IDS_STR = os.getenv("ADMIN_IDS", "123456789") # vergul bilan
try:
    ADMIN_IDS = [int(x.strip()) for x in ADMIN_IDS_STR.replace("***", "").split(",") if x.strip().isdigit()]
except:
    ADMIN_IDS = [123456789]

SHOP_NAME = "LOTEX SHOP"

# Tekshirish
if not BOT_TOKEN or "YOUR_REAL" in BOT_TOKEN:
    print("❌ XATO: BOT_TOKEN topilmadi! config.py ni to'g'irla")