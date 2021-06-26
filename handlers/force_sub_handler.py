# (c) @AbirHasan2005

from configs import Config
from pyrogram.errors import UserNotParticipant
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


async def handle_force_sub(bot, cmd):
    invite_link = await bot.create_chat_invite_link(int(Config.UPDATES_CHANNEL))
    try:
        user = await bot.get_chat_member(int(Config.UPDATES_CHANNEL), cmd.from_user.id)
        if user.status == "kicked":
            await bot.send_message(
                chat_id=cmd.from_user.id,
                text="Maaf kamu telah di ban karena melanggar peraturan kami hubungi [Support Group](https://t.me/linux_repo).",
                parse_mode="markdown",
                disable_web_page_preview=True
            )
            return 400
    except UserNotParticipant:
        await bot.send_message(
            chat_id=cmd.from_user.id,
            text="**Subscribe dulu baru bisa akses filenya**\n\n Klik tombol di bawah untuk subscribe",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("📥 Subscribe Sekarang 📥", url=invite_link.invite_link)
                    ],
                    [
                        InlineKeyboardButton("🔄 Refresh 🔄", callback_data="refreshmeh")
                    ]
                ]
            ),
            parse_mode="markdown"
        )
        return 400
    except Exception:
        await bot.send_message(
            chat_id=cmd.from_user.id,
            text="Ada yang salah hubungi [Support Group](https://t.me/linux_repo).",
            parse_mode="markdown",
            disable_web_page_preview=True
        )
        return 400
