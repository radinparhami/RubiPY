#  Pyrogram - Telegram MTProto API Client Library for Python
from rubipy.functions.session import Separator, SqliteSession
from rubipy.functions import auth


class SignIn:
    async def sign_in(
            self: "rubipy.client",
            phone_number: str,
            phone_code_hash: str,
            phone_code: str
    ) -> bool:
        phone_number = phone_number.strip(" +")

        invoke = await self.invoke(
            *auth.SignIn(
                phone_number=phone_number,
                phone_code_hash=phone_code_hash,
                phone_code=phone_code
            ).sign_in()
        )

        datas = Separator(invoke).session()
        SqliteSession(self.session_name).set_data(*datas)
        status, auth_key = invoke.status, datas[1]

        return (await self.invoke(
            auth.RegisterDevice(
                auth=auth_key
            ).register(),
            auth_key=auth_key,
            api_version='4'
        )).status
