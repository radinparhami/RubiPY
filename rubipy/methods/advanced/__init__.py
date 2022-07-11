#  Pyrogram - Telegram MTProto API Client Library for Python

from .authorize import Authorize
from .invoke import Invoke


class Advanced(
    Authorize,
    Invoke,
):
    pass
