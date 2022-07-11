from rubipy.functions import messages


class PinMessage:
    async def pin_message(
            self: "rubipy.Client",
            user_guid: str,
            message_id: int,

    ):
        return (await self.invoke(
            messages.SetPinMessage(
                user_guid,
                message_id,
                True,
            ).pin_message(),
        )).data.message_update

    async def unpin_message(
            self: "rubipy.Client",
            user_guid: str,
            message_id: int,

    ):
        return (await self.invoke(
            messages.SetPinMessage(
                user_guid,
                message_id,
                False,
            ).pin_message(),
        )).data.message_update
