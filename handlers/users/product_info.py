from loader import dp, db
from aiogram import types
from states.main import ShopState
from aiogram.dispatcher import FSMContext

@dp.callback_query_handler(state=ShopState.product)
async def get_product_info(call: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    sub_cat_id = data.get('sub_cat_id')
    product_slug = call.data
    info = db.get_product_info(subcategory_id=sub_cat_id, slug=product_slug)
    await call.message.answer_photo(photo=info[-3], caption=f"Mahsulot: {info[1]}\n\nNarx: {info[-4]}\n\nMa'lumot: {info[3]}")

