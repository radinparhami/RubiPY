#  Pyrogram - Telegram MTProto API Client Library for Python

from .sqlite_session import SqliteSession
from base64 import b64encode, b64decode
from json import dumps, loads


class SessionString:
    def __init__(self, session_string):
        self.session = session_string

    def encrypt(self):
        session = dumps(self.session).encode()
        return b64encode(session).decode()

    def decrypt(self):
        session = self.session.encode()
        return b64decode(session).decode()


class CQS:
    def __init__(
            self,
            session_name
    ):
        data = SqliteSession(session_name).get_data()
        phone_number, auth_key, user_guid = data
        self.data = dict(
            phone_number=phone_number,
            auth_key=auth_key,
            user_guid=user_guid
        )

    def string(self):
        return SessionString(self.data).encrypt()
