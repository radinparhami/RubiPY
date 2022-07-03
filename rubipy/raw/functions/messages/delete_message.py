#  Pyrogram - Telegram MTProto API Client Library for Python
from rubipy.client.values import InData


class DeleteMessage():  # type: ignore
    QUALNAME = "deleteMessages"

    def __init__(
            self,
            object_guid,
            message_ids,
            type,
    ):
        self.INPUT = dict(
            object_guid=object_guid,
            message_ids=message_ids,
            type=type,
        )

    def delete_message(self):
        return InData(self.QUALNAME, self.INPUT)
