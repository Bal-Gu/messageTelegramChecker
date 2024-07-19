from telethon import TelegramClient, events

api_id = 6899281
api_hash = '1e9512bf0c277a3d90669b308a39d7bb'
client = TelegramClient('anon', api_id, api_hash)


# -1002121499217
@client.on(events.NewMessage(chats=[-1002121499217]))
async def handler(event):
    print(event.raw_text)
    await client.send_message(-4241808181, event.raw_text)

@client.on(events.MessageEdited(chats=[-1002121499217]))
async def handler(event):
    original_message = event.original_update.message.raw_text
    await client.send_message(-4241808181, original_message)


client.start()
client.run_until_disconnected()
