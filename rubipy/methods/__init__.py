#  Pyrogram - Telegram MTProto API Client Library for Python

from rubipy.functions.session import SqliteToString
from .advanced import Invoke, Authorize
from .messages import Messages
from .users import Users
from .auth import Auth
from .chat import Chat


class Methods(
    SqliteToString,
    Authorize,
    Messages,
    Invoke,
    Users,
    Auth,
    Chat,
):
    pass
