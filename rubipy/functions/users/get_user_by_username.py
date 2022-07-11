#  Pyrogram - Telegram MTProto API Client Library for Python
from rubipy.crypto.values import InData


class GetUserByUsername():  # type: ignore
    QUALNAME = "getObjectByUsername"

    def __init__(
            self,
            username,
    ):
        self.INPUT = dict(
            username=username,
        )

    def get_user(self):
        return InData(self.QUALNAME, self.INPUT)
