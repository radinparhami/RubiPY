#  Pyrogram - Telegram MTProto API Client Library for Python

from .messages import Messages
from .advanced import Invoke
from .users import Users
from .auth import Auth


class Methods(
    Messages,
    Invoke,
    Users,
    Auth,
):
    pass
