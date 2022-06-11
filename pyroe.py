from pyrogram import Client
import pickle
import asyncio

api_id = 13788311 # your API ID here
api_hash = "e7b059c5b11752e4ce8a65822ef1c993"  # your API hash here
c = Client("my_pyrogram_session", api_id, api_hash)

async def main():
    await c.start()

    dialogs = [i async for i in c.get_dialogs()]

    chat_members = {}
    for i in dialogs:
        print("Loading", i.chat.id, i.chat.first_name or i.chat.title)
        try:
            members = [j async for j in i.chat.get_members()]
            chat_members[i.chat.id or i.chat.title] = members
            print(len(members), "member(s) loaded.")
        except Exception as e:
            print(e)

    with open("dialogs.pkl", "wb") as f:
        pickle.dump(dialogs, f)

    with open("members.pkl", "wb") as f:
        pickle.dump(chat_members, f)

asyncio.run(main())



