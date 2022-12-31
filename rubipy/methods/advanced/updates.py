#  Pyrogram - Telegram MTProto API Client Library for Python

from rubipy.raw.functions import data
from json import loads


class Updates:
    def __init__(self, method, response, cryption):
        self.method = method

        data_enc = response.json()['data_enc']
        load_datas = data.fromDict(
            loads(cryption.decrypt(data_enc))
        )
        error = load_datas.status_det
        if error and error != "OK":
            raise RuntimeError(error)
        self.res = load_datas

    def ret(self):
        self.sendMessage = self.res
        req = exec(f"self.{self.method}")
        print(req)

        return req or self.res
