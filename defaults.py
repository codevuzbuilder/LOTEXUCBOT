"""defaults.py - bot sozlamalari, tugmalar va matnlar"""
import os

# --- 1. ASOSIY SOZLAMALAR ---
SETTINGS = {
    "BOT_TOKEN": os.getenv("BOT_TOKEN", ""),
    "ADMIN_IDS": os.getenv("ADMIN_IDS", ""),
}

# --- 2. TUGMALAR MATNI ---
BUTTONS = {
    "catalog": "📦 Katalog",
    "cart": "🛒 Savat",
    "profile": "👤 Profil",
    "back": "⬅️ Ortga",
    "yes": "✅ Ha",
    "no": "❌ Yo'q",
    "admin": "⚙️ Admin",
}

# --- 3. BOT MATNLARI ---
TEXTS = {
    "start": "Assalomu alaykum! Xush kelibsiz.",
    "main_menu": "Asosiy menyu:",
    "not_found": "Topilmadi.",
    "error": "Xatolik yuz berdi, qaytadan urinib ko'ring.",
    "cart_empty": "Savatingiz bo'sh.",
    "profile": "Sizning profilingiz:",
}

# --- 4. NAMUNA / SAMPLE (ba'zi kodlar kutadi) ---
SAMPLE = {
    "currency": "so'm",
}

# Ba'zi eski kodlar TEXTS ni SETTINGS ichidan qidirishi mumkin, xavfsizlik uchun
# Agar boshqa nom kerak bo'lsa shu yerga qo'shing

