# (©)Codexbotz
# Recode by @mrismanaziz
# Modified by @SilenceSpe4ks
# t.me/SharingUserbot X t.me/infobotmusik


from config import FORCE_SUB_CHANNEL, FORCE_SUB_GROUP
from pyrogram.types import InlineKeyboardButton


def start_button(client):
    if not FORCE_SUB_CHANNEL and not FORCE_SUB_GROUP:
        buttons = [
            [
                InlineKeyboardButton(text="• ᴛᴇɴᴛᴀɴɢ sᴀʏᴀ •", callback_data="about"),
                InlineKeyboardButton(text="• ᴛᴜᴛᴜᴘ •", callback_data="close"),
            ],
            [
                InlineKeyboardButton(text="• TWITTER MIMIN •", url=f"https://twitter.com/omehot_tv"),
		InlineKeyboardButton(text="• VIP MURAH •", url=f"https://t.me/vip4646")
            ]
        ]
        return buttons
    if not FORCE_SUB_CHANNEL and FORCE_SUB_GROUP:
        buttons = [
            [
                InlineKeyboardButton(text="ʙᴇʀɢᴀʙᴜɴɢ", url=client.invitelink2),
            ],
            [
                InlineKeyboardButton(text="• ᴛᴇɴᴛᴀɴɢ sᴀʏᴀ •", callback_data="about"),
                InlineKeyboardButton(text="• ᴛᴜᴛᴜᴘ •", callback_data="close"),
            ],
            [
                InlineKeyboardButton(text="• TWITTER MIMIN •", url=f"https://twitter.com/omehot_tv"),
		InlineKeyboardButton(text="• VIP MURAH •", url=f"https://t.me/vip4646")
            ]
        ]
        return buttons
    if FORCE_SUB_CHANNEL and not FORCE_SUB_GROUP:
        buttons = [
            [
                InlineKeyboardButton(text="ʙᴇʀɢᴀʙᴜɴɢ", url=client.invitelink),
            ],
            [
                InlineKeyboardButton(text="• ᴛᴇɴᴛᴀɴɢ sᴀʏᴀ •", callback_data="about"),
                InlineKeyboardButton(text="• ᴛᴜᴛᴜᴘ •", callback_data="close"),
            ],
            [
                InlineKeyboardButton(text="• TWITTER MIMIN •", url=f"https://twitter.com/omehot_tv"),
		InlineKeyboardButton(text="• VIP MURAH •", url=f"https://t.me/vip4646")
            ]
        ]
        return buttons
    if FORCE_SUB_CHANNEL and FORCE_SUB_GROUP:
        buttons = [
            [
                InlineKeyboardButton(text="• ᴛᴇɴᴛᴀɴɢ sᴀʏᴀ •", callback_data="about"),
            ],
            [
                InlineKeyboardButton(text="• ᴊᴏɪɴ 1 •", url=client.invitelink),
                InlineKeyboardButton(text="• ᴊᴏɪɴ 2 •", url=client.invitelink2),
            ],
            [
                InlineKeyboardButton(text="• TWITTER MIMIN •", url=f"https://twitter.com/omehot_tv"),
		InlineKeyboardButton(text="• VIP MURAH •", url=f"https://t.me/vip4646")
            ],
            [InlineKeyboardButton(text="• ᴛᴜᴛᴜᴘ •", callback_data="close")],
        ]
        return buttons


def fsub_button(client, message):
    if not FORCE_SUB_CHANNEL and FORCE_SUB_GROUP:
        buttons = [
            [
                InlineKeyboardButton(text="ʙᴇʀɢᴀʙᴜɴɢ", url=client.invitelink2),
            ],
            [
                InlineKeyboardButton(text="• TWITTER MIMIN •", url=f"https://twitter.com/omehot_tv"),
		InlineKeyboardButton(text="• VIP MURAH •", url=f"https://t.me/vip4646")
            ]
        ]
        try:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text="ᴄᴏʙᴀ ʟᴀɢɪ",
                        url=f"https://t.me/{client.username}?start={message.command[1]}",
                    )
                ]
            )
        except IndexError:
            pass
        return buttons
    if FORCE_SUB_CHANNEL and not FORCE_SUB_GROUP:
        buttons = [
            [
                InlineKeyboardButton(text="ʙᴇʀɢᴀʙᴜɴɢ", url=client.invitelink),
            ],
            [
                InlineKeyboardButton(text="• TWITTER MIMIN •", url=f"https://twitter.com/omehot_tv"),
		InlineKeyboardButton(text="• VIP MURAH •", url=f"https://t.me/vip4646")
            ]
        ]
        try:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text="ᴄᴏʙᴀ ʟᴀɢɪ",
                        url=f"https://t.me/{client.username}?start={message.command[1]}",
                    )
                ]
            )
        except IndexError:
            pass
        return buttons
    if FORCE_SUB_CHANNEL and FORCE_SUB_GROUP:
        buttons = [
            [
                InlineKeyboardButton(text="• ᴊᴏɪɴ 1 •", url=client.invitelink),
                InlineKeyboardButton(text="• ᴊᴏɪɴ 2 •", url=client.invitelink2),
            ],
            [
                InlineKeyboardButton(text="• TWITTER MIMIN •", url=f"https://twitter.com/omehot_tv"),
		InlineKeyboardButton(text="• VIP MURAH •", url=f"https://t.me/vip4646")
            ]
        ]
        try:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text="ᴄᴏʙᴀ ʟᴀɢɪ",
                        url=f"https://t.me/{client.username}?start={message.command[1]}",
                    )
                ]
            )
        except IndexError:
            pass
        return buttons
