from rubipy.raw import functions


class EditMessage:
    async def edit_message(
            self: "rubipy.Client",
            user_guid: str,
            message_id: int,
            text: str,

    ):
        return (await self.invoke(
            functions.messages.EditMessage(
                object_guid=user_guid,
                message_id=message_id,
                text=str(text),
            ).edit_message(),
            auth_key=True,
        )).data.message_update
