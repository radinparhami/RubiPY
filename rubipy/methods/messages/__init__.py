#  Pyrogram - Telegram MTProto API Client Library for Python


from .delete_message import DeleteMessage
from .send_message import SendMessage
from .edit_message import EditMessage
from .pin_message import PinMessage


class Messages(
    DeleteMessage,
    SendMessage,
    EditMessage,
    PinMessage,
):
    pass
