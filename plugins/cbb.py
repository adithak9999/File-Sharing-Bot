#(©)Codexbotz

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>🤖 Bᴏᴛ Nᴀᴍᴇ: Sᴘɪᴅᴇʀᴍᴀɴ\n\n📝 Lᴀɴɢᴜᴀɢᴇ : Pʏᴛʜᴏɴ\n\n📚 Fʀᴀᴍᴇᴡᴏʀᴋ : Pʏʀᴏɢʀᴀᴍ\n\n📡 Hᴏsᴛᴇᴅ ᴏɴ : Rᴀɪʟᴡᴀʏ\n\n👨‍💻 Dᴇᴠᴇʟᴏᴘᴇʀ :  @SPIDERxTG\n\n💡 Sᴏᴜʀᴄᴇ Cᴏᴅᴇ : Cʟɪᴄᴋ Hᴇʀᴇ\n\n🔖 Qᴜᴏᴛᴇ : ആരും പേടിക്കേണ്ട എല്ലാവർക്കും കിട്ടും</b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🔒 Close", callback_data = "close")
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
