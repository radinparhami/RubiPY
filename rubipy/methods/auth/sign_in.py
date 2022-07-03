#  Pyrogram - Telegram MTProto API Client Library for Python
from rubipy.raw.functions.session import Separator, SqliteSession
from rubipy.raw import functions


class SignIn:
    async def sign_in(
            self: "rubipy.client",
            phone_number: str,
            phone_code_hash: str,
            phone_code: str
    ) -> bool:
        phone_number = phone_number.strip(" +")

        query = functions.auth.SignIn(
            phone_number=phone_number,
            phone_code_hash=phone_code_hash,
            phone_code=phone_code
        ).sign_in()
        invoke = await self.invoke(
            query=query,
            auth_key=query[-1]['tmp_session']
        )

        datas = Separator(invoke).session()
        SqliteSession(self.name).set_data(*datas)
        status, auth_key = invoke.status, datas[1]

        query = functions.auth.RegisterDevice(auth=auth_key).register()
        invoke = await self.invoke(
            query=query,
            auth_key=auth_key,
            api_version='4'
        )

        return status
