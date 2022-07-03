from rubipy.raw import functions


class SendCode():
    async def send_code(
            self: "rubipy.Client",
            phone_number: str
    ):
        phone_number = phone_number.strip(" +")

        try:
            query = functions.auth.SendCode(
                phone_number=phone_number,
            ).send_code()
            invoke = await self.invoke(
                query=query,
                auth_key=query[-1]['tmp_session']
            )

            data = dict(
                phone_code_hash=invoke.data.phone_code_hash,
                code_digits_count=invoke.data.code_digits_count,
            )
            return functions.data.fromDict(data)
        except Exception as error:
            raise error
