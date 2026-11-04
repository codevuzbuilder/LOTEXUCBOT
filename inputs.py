"""Admin uchun umumiy "matn kiriting" mexanizmi.""[span_21](start_span)"[span_21](end_span)
from aiogram import Router
from aiogram.filters import BaseFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from services import is_admin
from states import AdminS
from ui import A, Kb, show
# ... (input funksiyalari[span_22](start_span)[span_22](end_span))
