# RubiPY
> *Python Rubika Library* **[ 1.0 ]**

## Code
> Sample code to log into the user account and send a message

```python
from rubipy import Client
from asyncio import run

app = Client(session_name='Your_Session')


async def main():
    my_account = await app.get_me()
    await app.send_message(my_account.user_guid, "Hi")


run(main())
```

### **[Telegram Channel](https://t.me/RubiPY_Nots)**
