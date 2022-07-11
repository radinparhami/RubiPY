#  Pyrogram - Telegram MTProto API Client Library for Python

from rubipy.crypto.values import mach_phone_number
from rubipy.functions.session import SqliteSession


class Authorize:
    async def authorize(
            self: "rubipy.Client"
    ):
        if not self.phone_number:
            while True:
                value = input("Enter phone number :  ")

                if not value:
                    continue

                confirm = input(f'Is "{value}" correct? (y/N): ').lower()

                if confirm == "y":

                    self.phone_number = mach_phone_number(value)

                    try:
                        sent_code = await self.send_code(self.phone_number)
                        break
                    except Exception as error:
                        self.phone_number = None
                        error = str(error.args)
                        if "Max retries exceeded with url" in error:
                            print('\nYou have tried too much, please try again later\n'), exit()
                        else:
                            print(error)

        while True:
            if sent_code.status == 'SendPassKey':
                while True:
                    print("\n\t\tPassword hint: {}\n".format(sent_code.hint_pass_key))

                    if not self.password:
                        password = input("Enter password (empty to recover): ")

                        # if not self.password:
                        #     confirm = input("Confirm password recovery (y/n): ")
                        #
                        #     if confirm == "y":
                        #         email_pattern = await self.send_recovery_code()
                        #         print(f"The recovery code has been sent to {email_pattern}")
                        #
                        #         while True:
                        #             recovery_code = input("Enter recovery code: ")
                        #
                        #             return await self.recover_password(recovery_code)
                        #     else:
                        #         self.password = None
                        # else:
                        #     return await self.check_password(self.password)

                    sent_code = await self.send_code(
                        phone_number=self.phone_number,
                        pass_key=password,
                    )

                    if sent_code.status == 'OK':
                        self.password = password
                        break

            print(f"\nThe confirmation code has been sent via {sent_code.send_type}\n")

            while True:
                if not self.phone_code:
                    self.phone_code = input("Enter confirmation code: ")

                try:
                    signed_in = await self.sign_in(
                        self.phone_number,
                        sent_code.phone_code_hash,
                        self.phone_code
                    )
                except Exception as error:
                    print(str(error))
                    self.phone_code = None
                else:
                    self.datas = SqliteSession(self.session_name).get_data()
                    self.phone_number, self.auth_key, self.user_guid = self.datas
                    print("\n\nYou have successfully logged into your account\n")
                    await self.disconnect(), await self.start()
