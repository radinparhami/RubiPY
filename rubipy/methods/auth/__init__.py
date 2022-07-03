#  Pyrogram - Telegram MTProto API Client Library for Python


from .send_code import SendCode
from .sign_in import SignIn


class Auth(
    SendCode,
    SignIn,
):
    pass
