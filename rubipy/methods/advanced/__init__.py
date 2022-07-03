#  Pyrogram - Telegram MTProto API Client Library for Python

from .updates import Updates
from .invoke import Invoke


class Advanced(
    Updates,
    Invoke,
):
    pass
