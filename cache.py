"""Xotiradagi kesh: sozlamalar, tugma/matn o'zgartirishlari, premium emoji xaritasi.""[span_12](start_span)"[span_12](end_span)
import re

import db
from defaults import SETTINGS

UNSET = object()
settings: dict[str, str] = {}
buttons: dict[str, dict] = {}
texts: dict[str, dict] = {}
emap: dict[str, str] = {}
admins_db: set[int] = set()
emoji_rx: re.Pattern | None = None
# ... (qolgan qismi cache.py manba faylidan olingan[span_13](start_span)[span_13](end_span))
