#  Pyrogram - Telegram MTProto API Client Library for Python
from rubipy.client.values import InData, crypto, def_snd


class SendCode():  # type: ignore
    QUALNAME = "sendCode"

    def __init__(
            self,
            phone_number: str,
            send_type: str = "SMS"
    ):
        self.INPUT = dict(
            phone_number=phone_number,
            send_type=send_type
        )

    def send_code(self):
        return InData(self.QUALNAME, self.INPUT, tmp_session=def_snd())
