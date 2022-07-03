from rubipy.methods import Methods
from rubipy.raw import functions
from typing import Union
from asyncio import run
from .values import *


class Client(Methods):
    def __init__(
            self,
            session_name: str,
            phone_number: str = None,
            # phone_code: str = None,
            # password: str = None,
            auth_key: str = None,
            # session_string: str = None,
    ):

        self.session_name = session_name
        self.phone_number = phone_number
        # self.phone_code = phone_number
        # self.password = password
        self.auth_key = auth_key
        self.user_guid = None

        self.datas = functions.session.SqliteSession(session_name).get_data()

        if self.datas:
            self.phone_number, self.auth_key, self.user_guid = self.datas
        else:
            run(self.authorize())

    async def authorize(self):
        while True:
            try:
                if not self.phone_number:
                    while True:
                        value = input("Enter phone number :  ")

                        if not value:
                            continue

                        confirm = input(f'Is "{value}" correct? (y/N): ').lower()

                        if confirm == "y":
                            break

                    self.phone_number = value

                sent_code = await self.send_code(self.phone_number)
            except Exception as error:
                raise error
                self.phone_number = None
            else:
                break

        print(f"The confirmation code has been sent via SMS")

        while True:
            if not self.phone_code:
                self.phone_code = input("Enter confirmation code: ")

            try:
                signed_in = await self.sign_in(self.phone_number, sent_code.phone_code_hash, self.phone_code)
            except Exception as error:
                print(str(error))
                self.phone_code = None
            else:
                self.password = None
                self.datas = functions.session.SqliteSession(self.session_name).get_data()
                self.phone_number, self.auth_key, self.user_guid = self.datas
                print("You have successfully logged into your account")
                break

        return signed_in
