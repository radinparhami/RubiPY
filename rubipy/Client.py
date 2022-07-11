from .functions.session import SqliteSession, SessionString
from asyncio import run, get_event_loop
from .methods import Methods
from .Socket import Socket


class Client(Methods):
    def __init__(
            self,
            session_name: str,
            sqlite_session: tuple = None,
            session_string: str = None,
            phone_number: str = None,
            phone_code: str = None,
            password: str = None,
            auth_key: str = None,
            notif: bool = None,
    ):
        self.session_string = session_string
        self.session_name = session_name
        self.phone_number = phone_number
        self.phone_code = phone_code
        self.password = password
        self.auth_key = auth_key
        self.notif = notif

        self.connection = None
        self.handlers = dict()
        self.user_guid = None
        self.dcs = None

    def on_message(self, message: object):
        return lambda func: \
            self.add_handler(
                func, message
            )

    def add_handler(self, func, message: object):
        self.handlers.setdefault(func, message)

    def remove_handler(self, func):
        self.handlers.pop(func)

    async def __aenter__(self):
        return await self.start()

    async def __aexit__(self):
        return await self.disconnect()

    async def connect(self):
        self.connection = Socket(client=self)

    async def disconnect(self):
        return await self.connection.close()

    async def start(self):
        if self.session_string:
            session = SessionString(self.session_string).decrypt()
            self.session = session.values()
        else:
            self.session = SqliteSession(self.session_name).get_data()

        if self.session:
            self.phone_number, self.auth_key, self.user_guid = self.session
            await self.connect(), self.notif and print("\n\t\tStarted\n")
            return await self.connection.on_message()

        await self.connect(), await self.authorize()

    def run(self):
        run(self.start())
