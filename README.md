# RubiPY
> *Python Rubika Library* **[ 1.8 ]**

## Code
> Sample code to log into the user account and send a message

```python
from rubipy.crypto.values import InData, def_rnd
from rubipy import Client, Filters
from rubipy.types import Message

app = Client("my_account", notif=True)


@app.on_message(Filters.text & Filters.private)
async def receive_message(message: Message):
    message_id = message.message_id  # Message ID
    user_guid = message.user_guid  # Object Guid
    text = message.text  # Message Text

    await message.reply(f"Forwarding {text} ...", qute=True)

    input_data = dict(
        from_object_guid=user_guid,
        to_object_guid=user_guid,
        message_ids=[message_id],
        rnd=def_rnd(),
    )

    await app.invoke(
        InData(
            method="forwardMessages",  # Method Name
            INPUT=input_data,  # INPUT Data
        )
    )


app.run()
```

### **[Telegram Channel](https://t.me/RubiPY_Nots)**
