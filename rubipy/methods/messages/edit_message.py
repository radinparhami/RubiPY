from rubipy.functions import messages


class EditMessage:
    async def edit_message(
            self: "rubipy.Client",
            user_guid: str,
            message_id: int,
            text: str,

    ):
        return (await self.invoke(
            messages.EditMessage(
                object_guid=user_guid,
                message_id=message_id,
                text=str(text),
            ).edit_message(),
        )).data.message_update
