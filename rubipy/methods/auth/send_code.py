from rubipy.functions import auth
from rubipy.functions import data


class SendCode():
    async def send_code(
            self: "rubipy.Client",
            phone_number: str,
            pass_key: bool = None,
            send_type: str = 'SMS'
    ):
        try:
            sent_code = (await self.invoke(
                *auth.SendCode(
                    phone_number,
                    send_type,
                    pass_key,
                ).send_code()
            )).data
            sent_code.update(dict(send_type=send_type))

            return sent_code
        except Exception as error:
            raise error
