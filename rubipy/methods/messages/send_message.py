from rubipy.raw import functions


class SendMessage:
    async def send_message(
            self: "rubipy.Client",
            user_guid: str,
            text: str,
            reply_to_message_id: int = None,

    ):
        return (await self.invoke(
            functions.messages.SendMessage(
                reply_to_msg_id=reply_to_message_id,
                object_guid=user_guid,
                text=str(text),
            ).send_message(),
            auth_key=True,
        )).data.message_update
