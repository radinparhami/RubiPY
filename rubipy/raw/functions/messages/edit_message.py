#  Pyrogram - Telegram MTProto API Client Library for Python
from rubipy.client.values import InData


class EditMessage():  # type: ignore
    QUALNAME = "editMessage"

    def __init__(
            self,
            object_guid,
            message_id,
            text,
    ):
        self.INPUT = dict(
            object_guid=object_guid,
            message_id=message_id,
            text=text,
        )

    def edit_message(self):
        return InData(self.QUALNAME, self.INPUT)
