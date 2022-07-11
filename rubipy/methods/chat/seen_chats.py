from rubipy.functions import chat


class SeenChats:
    async def seen_chats(
            self: "rubipy.Client",
            seen_list: dict,

    ):
        return (await self.invoke(
            chat.SeenChats(
                seen_list,
            ).seen_chats(),
        )).data.message_update
