#  Pyrogram - Telegram MTProto API Client Library for Python
from rubipy.crypto.values import InData, crypto, def_snd


class SendCode():  # type: ignore
    QUALNAME = "sendCode"

    def __init__(
            self,
            phone_number,
            send_type,
            pass_key,
    ):
        self.INPUT = dict(
            phone_number=phone_number,
            send_type=send_type,
            pass_key=pass_key,
        )

    def send_code(self):
        auth_key = def_snd()
        return InData(self.QUALNAME, self.INPUT, tmp_session=auth_key), auth_key
