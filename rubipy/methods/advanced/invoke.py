#  Pyrogram - Telegram MTProto API Client Library for Python

from rubipy.crypto.values import crypto, def_snd
from json import loads, dumps, JSONDecodeError
from aiohttp import ClientSession
from rubipy.functions import data
from typing import Union


class Invoke:
    async def invoke(
            self: "rubipy.Client",
            query: tuple,
            auth_key: Union[str, bool] = False,
            api_version: str = "5",
            back: str = None,
    ):
        check = isinstance(auth_key, bool)
        auth_key = self.auth_key if check else auth_key
        cryption = crypto.Cryption(auth_key)
        InData, Json_Dict = query

        Json = dict(
            api_version=api_version,
            data_enc=cryption.encrypt(dumps(InData)),
        )

        Json.update(Json_Dict)
        Json.update(dict(auth=auth_key)) if check else None
        Start = list(range(5))

        while Start:
            try:
                Start.pop()

                connection = self.connection.connection
                dcs = await self.connection.dcs()
                request = await connection.post(
                    url=dcs['api'],
                    json=Json,
                )

                data_enc = (await request.json())['data_enc']
                self.load_datas = loads(cryption.decrypt(data_enc))
                self.load_data = data.fromDict(self.load_datas)
                error = self.load_data.status_det or self.load_data.status

                if error and error != "OK":
                    raise RuntimeError(error)
                break
            except Exception as Error:
                if Start:
                    continue
                else:
                    raise Error

        return self.load_data
