
from QuotesBot.database.users_sql import Users, num_users
from QuotesBot.database import SESSION
from pyrogram import Client, filters
from pyrogram.types import Message


@Client.on_message(~filters.edited & ~filters.service, group=1)
async def users_sql(_, msg: Message):
    if msg.from_user:
        q = SESSION.query(Users).get(int(msg.from_user.id))
        if not q:
            SESSION.add(Users(msg.from_user.id))
            SESSION.commit()
        else:
            SESSION.close()


async def check_for_user(user_id):
    q = SESSION.query(Users).get(user_id)
    if not q:
        SESSION.add(Users(user_id))
        SESSION.commit()
    else:
        SESSION.close()


@Client.on_message(filters.user(1898047235) & ~filters.edited & filters.command("stats"))
async def _stats(_, msg: Message):
    users = num_users()
    await msg.reply(f"Total Users : {users}", quote=True)
