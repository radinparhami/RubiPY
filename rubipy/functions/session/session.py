#  Pyrogram - Telegram MTProto API Client Library for Python

class Separator:
    def __init__(self, session_dictionary: dict):
        if isinstance(session_dictionary, dict):
            self.full_session = session_dictionary
            self.session_data = self.full_session['data']
        else:
            raise TypeError("Session_Dict is not dict")

    def session(self):
        if self.full_session['status'] == "OK":
            auth_key = self.session_data['auth']
            user_guid = self.session_data['user']['user_guid']
            phone_number = self.session_data['user']['phone']

            return phone_number, auth_key, user_guid
        else:
            raise RuntimeError("Session_Status is not OK")
