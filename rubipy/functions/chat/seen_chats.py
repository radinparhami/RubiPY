#  Pyrogram - Telegram MTProto API Client Library for Python
from rubipy.crypto.values import InData


class SeenChats():  # type: ignore
    QUALNAME = "seenChats"

    def __init__(
            self,
            seen_list,
    ):
        self.INPUT = dict(
            seen_list=seen_list
        )

    def seen_chats(self):
        return InData(self.QUALNAME, self.INPUT)
