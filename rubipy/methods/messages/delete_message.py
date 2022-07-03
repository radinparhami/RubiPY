from rubipy.raw import functions
from typing import Union


class DeleteMessage:
    async def delete_message(
            self: "rubipy.Client",
            user_guid: str,
            message_ids: Union[int, list],
            type: str = "Global",

    ):
        message_ids = [message_ids] if \
            isinstance(message_ids, str) else message_ids
        return (await self.invoke(
            functions.messages.DeleteMessage(
                object_guid=user_guid,
                message_ids=message_ids,
                type=type,
            ).delete_message(),
            auth_key=True,
        )).data
