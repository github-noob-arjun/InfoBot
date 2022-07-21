import os
from datetime import datetime
from pyrogram import Client, filters
from pyrogram.types import User, InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.raw import functions
from pyrogram.errors import PeerIdInvalid


BUTTON_1 = InlineKeyboardMarkup( [[
       InlineKeyboardButton("✅ 𝗝𝗼𝗶𝗻 𝗡𝗼𝘄 ✅", url="https://t.me/PyroBotz")
       ]]
       )

@IDBot.on_message(filters.private & filters.command("id"))
async def id_handler(bot, update):
    if message.reply_to_message:
        if message.reply_to_message.sticker:
           await message.reply(f"**𝐘𝐨𝐮𝐫 𝐒𝐭𝐢𝐜𝐤𝐞𝐫 𝐈𝐃 :-**  \n `{message.reply_to_message.sticker.file_id}` \n \n ** Unique ID is ** \n\n`{message.reply_to_message.sticker.file_unique_id}`", quote=True)
        if message.reply_to_message.photo:
           await message.reply(f"**𝐘𝐨𝐮𝐫 𝐏𝐡𝐨𝐭𝐨 𝐈𝐃 :-**  \n `{message.reply_to_message.photo.file_id}` \n \n ** Unique ID is ** \n\n`{message.reply_to_message.photo.file_unique_id}`", quote=True)
        if message.reply_to_message.video:
           await message.reply(f"**𝐘𝐨𝐮𝐫 𝐕𝐢𝐝𝐞𝐨 𝐈𝐃 :-**  \n `{message.reply_to_message.video.file_id}` \n \n ** Unique ID is ** \n\n`{message.reply_to_message.video.file_unique_id}`", quote=True)
        if message.reply_to_message.animation:
           await message.reply(f"**𝐘𝐨𝐮𝐫 𝐀𝐧𝐢𝐦𝐚𝐭𝐢𝐨𝐧 𝐈𝐃 :-**  \n `{message.reply_to_message.animation.file_id}` \n \n ** Unique ID is ** \n\n`{message.reply_to_message.animation.file_unique_id}`", quote=True)
        if message.reply_to_message.audio:
           await message.reply(f"**𝐘𝐨𝐮𝐫 𝐀𝐮𝐝𝐢𝐨 𝐈𝐃 :-**  \n `{message.reply_to_message.audio.file_id}` \n \n ** Unique ID is ** \n\n`{message.reply_to_message.audio.file_unique_id}`", quote=True)
        if message.reply_to_message.video_note:
           await message.reply(f"**𝐘𝐨𝐮𝐫 𝐕𝐢𝐝𝐞𝐨 𝐍𝐨𝐭𝐞 𝐈𝐃 :-**  \n `{message.reply_to_message.video_note.file_id}` \n \n ** Unique ID is ** \n\n`{message.reply_to_message.video_note.file_unique_id}`", quote=True)
        if message.reply_to_message.voice:
           await message.reply(f"**𝐘𝐨𝐮𝐫 𝐕𝐨𝐢𝐜𝐞 𝐈𝐃 :-**  \n `{message.reply_to_message.voice.file_id}` \n \n ** Unique ID is ** \n\n`{message.reply_to_message.voice.file_unique_id}`", quote=True)
    else:
        await update.reply_text(        
            text="🆔 𝚈𝚘𝚞𝚛 𝙸𝙳 :- {update.from_user.id}",
            disable_web_page_preview=True,
            reply_markup=BUTTON_1
        )
@IDBot.on_message(filters.group & filters.command("id"))
async def id_handler(bot, update):
    await update.reply_text(        
        text="**🆔 𝚈𝚘𝚞𝚛 𝙸𝙳 :-** `{update.from_user.id}`\n\n**💬 𝚃𝚑𝚒𝚜 𝙲𝚑𝚊𝚝 𝙸𝙳 :-** `{update.chat.id}`",
        disable_web_page_preview=True,
        reply_markup=BUTTON_1
    )
@IDBot.on_message(filters.private & filters.forwarded)
async def info(motech, msg):
    if msg.forward_from:
        text = "<u>𝐅𝐨𝐫𝐰𝐚𝐫𝐝 𝐈𝐧𝐟𝐨𝐫𝐦𝐚𝐭𝐢𝐨𝐧 👀</u> \n\n"
        if msg.forward_from["is_bot"]:
            text += "<u>🤖 𝐁𝐨𝐭 𝐈𝐧𝐟𝐨</u>"
        else:
            text += "<u>👤𝐔𝐬𝐞𝐫 𝐈𝐧𝐟𝐨</u>"
        text += f'\n\n👨‍💼 𝐍𝐚𝐦𝐞 : {msg.forward_from["first_name"]}'
        if msg.forward_from["username"]:
            text += f'\n\n🔗 𝐔𝐬𝐞𝐫𝐍𝐚𝐦𝐞 : @{msg.forward_from["username"]} \n\n🆔 ID : <code>{msg.forward_from["id"]}</code>'
        else:
            text += f'\n\n🆔 𝐈𝐃 : `{msg.forward_from["id"]}`'
        pfp = await motech.get_profile_photos(msg.forward_from["id"])
        if not pfp:
            await msg.reply(text, quote=True)
        else:
            dls = await motech.download_media(pfp[0]["file_id"], file_name=f"{msg.forward_from["id"]}.png")
            await msg.reply_photo(
                photo=dls,
                caption=text,
                quote=True
            )
            os.remove(dls)
    else:
        hidden = msg.forward_sender_name
        if hidden:
            await msg.reply(
                f"❌️𝐄𝐫𝐫𝐨𝐫 <b><i>{hidden}</i></b> ❌️𝐄𝐫𝐫𝐨𝐫",
                quote=True,
            )
        else:
            text = f"<u>𝐅𝐨𝐫𝐰𝐚𝐫𝐝 𝐈𝐧𝐟𝐨𝐫𝐦𝐚𝐭𝐢𝐨𝐧 👀</u>.\n\n"
            if msg.forward_from_chat["type"] == "channel":
                text += "<u>📢 𝐂𝐡𝐚𝐧𝐧𝐞𝐥</u>"
            if msg.forward_from_chat["type"] == "supergroup":
                text += "<u>🗣️ 𝐆𝐫𝐨𝐮𝐩</u>"
            text += f'\n\n📃 𝐍𝐚𝐦𝐞 {msg.forward_from_chat["title"]}'
            if msg.forward_from_chat["username"]:
                text += f'\n\n➡️ 𝐅𝐫𝐨𝐦 : @{msg.forward_from_chat["username"]}'
                text += f'\n\n🆔 𝐈𝐃 : `{msg.forward_from_chat["id"]}`'
            else:
                text += f'\n\n🆔 𝐈𝐃 `{msg.forward_from_chat["id"]}`\n\n'
            await msg.reply(text, quote=True)

