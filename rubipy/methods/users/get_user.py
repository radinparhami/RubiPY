from rubipy.functions import users
from typing import Union
from re import findall


class GetUser:
    async def get_user(
            self: "rubipy.Client",
            username: str,

    ):
        pattern = "(@\D\w+)"
        user_name = findall(pattern, username)
        if user_name:
            return (await self.invoke(
                users.GetUserByUsername(
                    username=user_name[0][1:]
                ).get_user(),
            )).data.user
        else:
            return (await self.invoke(
                GetUser(
                    object_guid=username,
                ).get_user(),
            )).data.user

