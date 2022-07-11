#  Pyrogram - Telegram MTProto API Client Library for Python

from sqlite3 import connect


class SqliteSession:
    def __init__(
            self,
            session_name: str,
            format: str = 'session'
    ):
        self.session = session_name + '.' + format
        self.data_base = connect(self.session)
        self.cursor = self.data_base.cursor()

        self.cursor.execute(
            'create table if not exists session'
            ' (phone_number text primary key,'
            ' auth_key text,'
            ' user_guid text)'
        )

    def set_data(self, phone_number, auth, guid):
        self.cursor.execute(
            'insert or replace into session'
            ' (phone_number, auth_key, user_guid)'
            ' values (?, ?, ?)',
            (phone_number, auth, guid)
        )
        self.data_base.commit(), self.cursor.close()
        return self.session

    def get_data(self):
        try:
            self.cursor.execute('select * from session')
            result = self.cursor.fetchone(), self.cursor.close()
            return result[0]
        except:
            return None


class StringToSqlite:
    def __init__(
            self,
            session_name,
            session_string,
    ):
        self.session_dictionary = SessionString(session_string).decrypt()
        self.data = Separator(session_dictionary=self.session_dictionary)
        self.session_name: str = session_name

    def sqLite(self):
        return SqliteSession(self.session_name).set_data(*self.data)
