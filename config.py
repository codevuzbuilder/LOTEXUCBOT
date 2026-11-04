import os

# Token GitHub Secrets dan olinadi
BOT_TOKEN = os.getenv("BOT_TOKEN")

# Localda test qilmoqchi bo'lsang tokeningni shu yerga yoz (faqat local uchun)
if not BOT_TOKEN or len(BOT_TOKEN) < 20 or "***" in BOT_TOKEN:
    BOT_TOKEN = "BU_YERGA_BOT_TOKENINGNI_YOZ"  # Masalan: 123456:AAH...

# SENING ADMIN IDING - TO'G'RILANDI
ADMIN_IDS = [8828687079]

# Qo'shimcha adminlar kerak bo'lsa vergul bilan qo'sh:
# ADMIN_IDS = [8828687079, 123456789]

SHOP_NAME = "LOTEX SHOP"

print(f"✅ Config yuklandi | ADMIN: {ADMIN_IDS}")