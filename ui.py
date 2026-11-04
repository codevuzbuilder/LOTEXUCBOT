"""Interfeys: rangli tugmalar, premium emoji, matn/media yuborish.""[span_16](start_span)"[span_16](end_span)
import html
import logging
import re
from dataclasses import dataclass

from aiogram.exceptions import TelegramBadRequest
from aiogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup, Message

import cache
from defaults import BUTTONS, SAMPLE, TEXTS
# ... (qolgan interfeys funksiyalari[span_17](start_span)[span_17](end_span))
