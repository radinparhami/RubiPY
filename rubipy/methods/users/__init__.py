#  Pyrogram - Telegram MTProto API Client Library for Python

from .get_user import GetUser
from .get_me import GetMe

class Users(
    GetUser,
    GetMe,
):
    pass
