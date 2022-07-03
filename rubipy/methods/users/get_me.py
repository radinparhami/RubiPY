from rubipy.raw import functions
from typing import Union


class GetMe:
    async def get_me(
            self: "rubipy.Client",
    ):
        return (await self.invoke(
            functions.users.GetUser(
                object_guid=self.user_guid
            ).get_user(),
            auth_key=True,
        )).data.user
