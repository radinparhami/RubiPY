from rubipy.crypto.values import Global, Local
from rubipy.functions import messages
from typing import Union


class DeleteMessage:
    async def delete_message(
            self: "rubipy.Client",
            user_guid: str,
            message_ids: Union[int, list],
            global_delete: bool = True,

    ):
        message_ids = message_ids if isinstance(
            message_ids, list) else [message_ids]
        return (await self.invoke(
            messages.DeleteMessage(
                object_guid=user_guid,
                message_ids=message_ids,
                type=Global if global_delete else Local,
            ).delete_message(),
        )).data
