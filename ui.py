"""Interfeys: rangli tugmalar, premium emoji, matn/media yuborish."""
import html
import logging
import re
from dataclasses import dataclass

from aiogram.exceptions import TelegramBadRequest
from aiogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup, Message

import cache
from defaults import BUTTONS, SAMPLE, TEXTS
# ... (qolgan interfeys funksiyalari)