from string import ascii_lowercase, digits
from random import randint, choice
from rubipy.crypto import crypto
from typing import Union
from json import dumps


def gnerator(number):
    pattern = ascii_lowercase
    function = lambda jey: choice(pattern)
    iteration = map(function, range(number))

    return str().join(list(iteration))


defaultDevice = {
    "device_hash": "25010064645373610200053736",
    "system_version": "Windows 10",
    "device_model": "Chrome 102",
    "app_version": "WB_4.0.7",
    "token_type": "Web",
    "lang_code": "fa",
    "token": '',
}

defaultPlatform = {
    'platform': 'Web',
    'lang_code': "fa",
    'app_name': 'Main',
    'app_version': '4.0.7',
    'package': 'web.rubika.ir',
    'user_agent': ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                   'AppleWebKit/537.36 (KHTML, like Gecko)'
                   'Chrome/102.0.0.0 Safari/537.36'),
}


def mach_phone_number(phone_number: str):
    phone_number = phone_number[-10:]

    if phone_number and digits[-1] == phone_number[0]:
        return digits[:-3:-1] + phone_number

    raise ValueError(
        '\nPlease enter the phone number '
        'like this\n\n\t\t\t98 xxx xxx xxxx\n'
    )


GetCMESS_URL = "https://getdcmess.iranlms.ir/"
Global, Local = "Global", "Local"
Pin, UnPin = "Pin", "Unpin"

def_int = 100000, 999999999
def_snd = lambda: gnerator(32)
def_cac = ["data", "message_update"]
def_rnd = lambda: str(randint(*def_int))
def_url = "https://messengerg2c{}.iranlms.ir/"
def_get = lambda: def_url.format(randint(10, 99))

message = {
    'object_guid': str(),
    'rnd': def_rnd(), 'text': str(),
    'reply_to_message_id': None or str()
}

Json = {
    "api_version": "5",
    "auth": str(), "data_enc": str()}


def InData(
        method: Union[str, tuple],
        INPUT: dict, client=defaultPlatform,
        **json
):
    if isinstance(method, tuple):
        enc = INPUT
        json.update(
            dict(
                method=method[0],
                client=client,
            )
        )
    else:
        enc = {
            'method': method,
            'input': INPUT,
            'client': client,
        }

    return enc, json
