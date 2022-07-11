from rubipy.functions import users
from typing import Union


class GetMe:
    async def get_me(
            self: "rubipy.Client",
    ):
        return (await self.invoke(
            users.GetUser(
                object_guid=self.user_guid
            ).get_user(),
        )).data.user
