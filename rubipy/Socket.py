from .types import Message, Delete_Message, Event
from rubipy.crypto.values import defaultPlatform
from aiohttp import ClientTimeout, ClientSession
from rubipy.crypto.values import GetCMESS_URL
from .crypto.crypto import Cryption
from rubipy.functions import data
from json import dumps, loads


class Socket:
    def __init__(self, client):
        self.client = client
        self.auth = client.auth_key
        self.handlers = client.handlers
        self.connection = ClientSession(
            headers={'user-agent': defaultPlatform['user_agent']},
            timeout=ClientTimeout(total=20))

    async def dcs(self):
        response = await self.connection.post(GetCMESS_URL)
        response = await response.json()
        data = response['data']

        socket, api = data['socket'], data['API']
        default_sockets = list(socket.values())
        default_apis = list(api.values())

        return dict(
            sockets=default_sockets[:3],
            api=default_apis[0],
        )

    async def close(self):
        await self.connection.close()

    async def on_message(self):
        dcs = await self.dcs()

        try:
            for url in dcs['sockets']:
                async with self.connection.ws_connect(url) as wss:
                    await wss.send_json({
                        'method': 'handShake',
                        'auth': self.auth,
                        'api_version': '5'})
                    async for message in wss:
                        try:
                            result = message.json()
                            data_enc = result.get('data_enc')
                            if data_enc:
                                result = Cryption(self.auth).decrypt(data_enc)
                                updates = data().fromDict(loads(result))
                                message_updates = updates.message_updates

                                if message_updates and message_updates[0].action:
                                    message_updates = message_updates[0]
                                    action = message_updates.action
                                    event_update = None

                                    if action in ["New", "Edit"]:
                                        message: Message = Message(
                                            self.client,
                                            message_updates
                                        )
                                        event = message_updates.message.event_data
                                        message_update: Event = Event(event) if event else message
                                    elif action == "Delete":
                                        message_update: Delete_Message = Delete_Message(
                                            message_updates
                                        )

                                    for func, handler in self.handlers.items():
                                        if await handler(self, message_update) and isinstance(message_update, Message):
                                            await func(message_update)
                            else:
                                pass

                        except Exception as error:
                            print(error)
        except KeyError:
            pass
