#  Pyrogram - Telegram MTProto API Client Library for Python
from rubipy.crypto.values import InData, Pin, UnPin


class SetPinMessage():  # type: ignore
    QUALNAME = "setPinMessage"

    def __init__(
            self,
            object_guid,
            message_id,
            action,
    ):
        self.INPUT = dict(
            action=Pin if action else UnPin,
            object_guid=object_guid,
            message_id=message_id,
        )

    def pin_message(self):
        return InData(self.QUALNAME, self.INPUT)
