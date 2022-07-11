from rubipy import Client


class Message:
    def __init__(self, client, update: dict):
        if update.action:
            self.action: str = update.action
            self.chat_type: str = update.type

        self.client: Client = client
        self.message: dict = update.message
        self.text: str = update.message.text
        self.user_guid: str = update.object_guid
        self.message_type: str = self.message.type
        self.unix_time: int = int(update.timestamp)
        self.message_id: int = int(update.message_id)
        self.author_type: str = self.message.author_type
        self.is_edited: bool = bool(self.message.is_edited)
        reply_to_message_id = self.message.reply_to_message_id
        self.author_user_guid: str = self.message.author_object_guid
        self.updated_parameters: list = self.message.updated_parameters
        self.is_self: bool = self.client.user_guid == self.message.author_object_guid
        self.reply_to_message_id: int = reply_to_message_id and int(reply_to_message_id)

    '''
        auto send message :

            args :
                text, qute :
                    text :
                             Text Message        |  String
                    qute :
                        auto reply to message id |  Boolean
        '''

    async def reply(self, text, qute=None):
        return await self.client.send_message(
            user_guid=self.user_guid, text=text,
            reply_to_message_id=qute and self.message_id,
        )

    async def edit(self, text):
        return await self.client.edit_message(
            user_guid=self.user_guid,
            message_id=self.message_id,
            text=text
        )

    async def delete(self, Global=True):
        return await self.client.delete_message(
            user_guid=self.user_guid,
            message_ids=self.message_id,
            global_delete=Global
        )

    async def pin(self):
        return await self.client.pin_message(
            user_guid=self.user_guid,
            message_id=self.message_id,
        )

    async def seen(self):
        seen_list = {self.user_guid: self.message_id}
        return await self.client.seen_chats(
            seen_list=seen_list
        )


class Delete_Message:
    def __init__(self, update: dict):
        self.action: str = update.action
        self.chat_type: str = update.type
        self.user_guid: str = update.object_guid
        self.message_id: int = int(update.message_id)
