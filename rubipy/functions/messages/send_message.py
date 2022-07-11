#  Pyrogram - Telegram MTProto API Client Library for Python
from rubipy.crypto.values import InData, def_rnd


class SendMessage():  # type: ignore
    QUALNAME = "sendMessage"

    def __init__(
            self,
            reply_to_msg_id,
            object_guid,
            text,
    ):
        self.INPUT = dict(
            reply_to_message_id=reply_to_msg_id,
            object_guid=object_guid,
            rnd=def_rnd(),
            text=text,
        )

    def send_message(self):
        return InData(self.QUALNAME, self.INPUT)
