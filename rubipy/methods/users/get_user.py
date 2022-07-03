from rubipy.raw import functions
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
                functions.users.GetUserByUsername(
                    username=user_name[0][1:]
                ).get_user(),
                auth_key=True,
            )).data.user
        else:
            return (await self.invoke(
                functions.users.GetUser(
                    object_guid=username,
                ).get_user(),
                auth_key=True,
            )).data.user

