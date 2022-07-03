#  Pyrogram - Telegram MTProto API Client Library for Python
from rubipy.client.values import InData, crypto, def_snd


class SignIn():  # type: ignore
    QUALNAME = "signIn"

    def __init__(
            self,
            phone_number: str,
            phone_code_hash: str,
            phone_code: str,
    ):
        self.INPUT = dict(
            phone_number=phone_number,
            phone_code_hash=phone_code_hash,
            phone_code=phone_code,
        )

    def sign_in(self):
        return InData(self.QUALNAME, self.INPUT, tmp_session=def_snd())
