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



def about_product(url, product_id):
    numbers = InlineKeyboardMarkup(row_width=3)
    for i in range(1, 10):
        numbers.insert(InlineKeyboardButton(text=i, callback_data=i))
    btn1 = InlineKeyboardButton(text="❤️ Saqlash", callback_data="like")
    btn2 = InlineKeyboardButton(text="🔗 Batafsil", url=url)
    numbers.add(btn1, btn2)
    numbers.add(back, home)
    return numbers

def get_all_cats(cats_info):
    markup = InlineKeyboardMarkup(row_width=2)
    for cat in cats_info:
        markup.insert(InlineKeyboardButton(text=cat[1], callback_data=cat[2]))
    markup.add(back, home)
    return markup
