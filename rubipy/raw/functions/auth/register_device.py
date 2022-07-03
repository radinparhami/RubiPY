#  Pyrogram - Telegram MTProto API Client Library for Python
from rubipy.client.values import defaultDevice, InData, crypto
from json import dumps


class RegisterDevice():  # type: ignore
    QUALNAME = "registerDevice"

    def __init__(
            self,
            auth: str,
            device: dict = defaultDevice,
    ):
        self.auth = auth

    def register(self):
        return InData(
            (self.QUALNAME, True),
            defaultDevice,
            auth=self.auth
        )
