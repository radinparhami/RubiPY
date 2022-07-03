from base64 import b64encode, urlsafe_b64decode
from Crypto.Util.Padding import pad, unpad
from string import ascii_lowercase as word
from Crypto.Cipher import AES


class Cryption:
    def __init__(self, auth):
        self.key = bytearray(self.secret(auth), "UTF-8")
        self.iv = bytearray.fromhex("0" * 32)

    def secret(self, text):
        text = text[16:24] + text[:8] + text[24:32] + text[8:16]
        secret_iter = lambda index: word[(ord(index) - 10) % 26]
        return str().join(list(map(secret_iter, text)))

    def encrypt(self, text):
        Raw = pad(text.encode(), AES.block_size)
        Ase = AES.new(self.key, AES.MODE_CBC, self.iv)
        Enc = b64encode(Ase.encrypt(Raw))
        return Enc.decode()

    def decrypt(self, text):
        Enc = text.encode()
        Aes = AES.new(self.key, AES.MODE_CBC, self.iv)
        Decrypt_Point = Aes.decrypt(urlsafe_b64decode(Enc))
        return unpad(Decrypt_Point, AES.block_size).decode()
