"""Xotiradagi kesh: sozlamalar, tugma/matn o'zgartirishlari, premium emoji xaritasi."""
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
