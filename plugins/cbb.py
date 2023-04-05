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
            text = f"🤖 Bᴏᴛ Nᴀᴍᴇ: sᴘɪᴅᴇʀᴍᴀɴ\n\n📝 Lᴀɴɢᴜᴀɢᴇ : ᴘʏᴛʜᴏɴ\n\n📚 Fʀᴀᴍᴇᴡᴏʀᴋ : ᴘʏʀᴏɢʀᴀᴍ\n\n📡 Hᴏsᴛᴇᴅ ᴏɴ : ʜᴇʀᴏᴋᴜ\n\n👨‍💻 Dᴇᴠᴇʟᴏᴘᴇʀ :  ᴀᴅɪᴛʜ ᴛɢ 🇮🇳\n\n💡 Sᴏᴜʀᴄᴇ Cᴏᴅᴇ : ᴄʟɪᴄᴋ ʜᴇʀᴇ\n\n🔖 Qᴜᴏᴛᴇ : ആരും പേടിക്കേണ്ട എല്ലാവർക്കും കിട്ടും",
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
