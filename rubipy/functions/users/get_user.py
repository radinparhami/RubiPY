#  Pyrogram - Telegram MTProto API Client Library for Python
from rubipy.crypto.values import InData


class GetUser():  # type: ignore
    QUALNAME = "getUserInfo"

    def __init__(
            self,
            object_guid,
    ):
        self.INPUT = dict(
            object_guid=object_guid,
        )

    def get_user(self):
        return InData(self.QUALNAME, self.INPUT)
