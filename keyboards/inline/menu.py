from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

main_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="All Categories", callback_data="cats")],
        [InlineKeyboardButton(text="🛒 Cart", callback_data="cart"), InlineKeyboardButton(text="Orders", callback_data="orders")],
        [InlineKeyboardButton(text="Search", callback_data="search"), InlineKeyboardButton(text="Settings", callback_data="settings")]
    ]
)

back = InlineKeyboardButton(text="Orqaga", callback_data="back")
home = InlineKeyboardButton(text="Bosh sahifa", callback_data="home")
