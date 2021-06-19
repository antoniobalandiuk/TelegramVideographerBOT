from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from config import TOKEN

bot = Bot(token=TOKEN)
db = Dispatcher(bot)


def callback(menu_name, message_text, keyboard):
    @db.callback_query_handler(text_container=menu_name)
    async def menu(call: types.CallbackQuery):
        await call.message.edit_text(message_text, reply_markup=keyboard)
