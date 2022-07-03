#  Pyrogram - Telegram MTProto API Client Library for Python

from rubipy.client.values import crypto, def_get, def_snd
from json import loads, dumps, JSONDecodeError
from rubipy.raw.functions import data
from requests import post


class Invoke:
    async def invoke(
            self: "rubipy.Client",
            query: tuple,
            auth_key: str,
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
                request = post(
                    url=def_get(),
                    json=Json,
                    timeout=5
                )
                data_enc = request.json()['data_enc']
                load_datas = data.fromDict(loads(cryption.decrypt(data_enc)))
                error = load_datas.status_det
                if error and error != "OK":
                    raise RuntimeError(error)
                else:
                    return load_datas
            except Exception as Error:
                if Start:
                    continue
                else:
                    raise Error
