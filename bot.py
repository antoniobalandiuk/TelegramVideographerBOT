import asyncio

from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

keyboard = InlineKeyboardMarkup()
services = InlineKeyboardButton(text='Види послуг 🎥', callback_data="services")
price = InlineKeyboardButton(text='Прайс-лист 💵', callback_data="price")
contacts = InlineKeyboardButton(text='Контактні дані 👥', callback_data="contacts")
special_offers = InlineKeyboardButton(text='Особливі пропозиції 🤝', callback_data="special_offers")
reviews = InlineKeyboardButton(text='Відгуки', callback_data="reviews")
keyboard.add(services, price, contacts, special_offers, reviews)


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply(f'Привіт! Я - відеомейкер з почуттям стилю!🎞🎥\n\n'
                        f'Я – Анатолій Ружицький, мені 16 років👦. \"16?! Та ти обманюєш!\" - часто чую такі реакції з боку своїх клієнтів, які вподальшому говорять: \"Вірний своїй справі, вірний своїм переконанням, бомбезний оператор, в якого все ще попереду!\n\n'
                        f'Моя робота — створити приємні спогади, відтворити атмосферу подій на природі🛤, у місті🌇 чи студії🎼, запам`ятати усі емоції в кадрах.',
                        reply_markup=keyboard)


# const callbacks = {
#     menu: () => {},
#     price: () => {},
#     default: () =>
# };
#
#  callbacks[call](ьуыыфпу) || [default]


# Callbecks for telegram call : string

# @dp.callback_query_handler(text_contains='menu_')
# async def menu(call: types.CallbackQuery):
#     if call.data and call.data.startswith("menu_"):
#         code = call.data[-1:]
#         if code.isdigit():
#             code = int(code)
#         if code == 1:
#             await call.message.edit_text(f'Тут будуть послуги, моделі камер та дрону', reply_markup=keyboard)
#         if code == 2:
#             await call.message.edit_text(f'🎞  Кліпи - від 200💲\n\n'
#                                          f'👗  Fashion - від 100💲\n\n'
#                                          f'🗣  Рекламні відео - від 100💲\n\n'
#                                          f'💍  Весільні фільми - є кілька пакетів, залежно від кількості знімальних годин, камер та наявності аерозйомки\n\n'
#                                          f'💏  Love Story - 100💲\n\n'
#                                          f'✈  Аерозйомка - від 50💲\n\n'
#                                          f'👨‍💻  Монтаж - від 30💲\n\n', reply_markup=keyboard)
#         if code == 3:
#             await call.message.edit_text(f'📱Моб.тел - +380975547372\n\n'
#                                          f'Instagram - @tolian_ruzhytskyi\n\n'
#                                          f'Telegram - @tolian_ruzhytskyi\n\n', reply_markup=keyboard)
#         if code == 4:
#             await call.message.edit_text(f'Я є прибічником збалансованого обміну\n'
#                                          f'послугами або ж товарами, тому якщо\n'
#                                          f'у вас є вигідна бартерна пропозиція,\n'
#                                          f'то дзвоніть по номеру телефону, що\n'
#                                          f'вказаний у меню "Контактні дані 👥"\n', reply_markup=keyboard)
#         else:
#             await bot.answer_callback_query(call.id)


@dp.callback_query_handler(text_contains='services')
async def menu(call: types.CallbackQuery):
    await call.message.edit_text(f'Тут будуть послуги, моделі камер та дрону', reply_markup=keyboard)


@dp.callback_query_handler(text_contains='price')
async def menu(call: types.CallbackQuery):
    await call.message.edit_text(f'🎞  Кліпи - від 200💲\n\n'
                                 f'👗  Fashion - від 100💲\n\n'
                                 f'🗣  Рекламні відео - від 100💲\n\n'
                                 f'💍  Весільні фільми - є кілька пакетів, залежно від кількості знімальних годин, камер та наявності аерозйомки\n\n'
                                 f'💏  Love Story - 100💲\n\n'
                                 f'✈  Аерозйомка - від 50💲\n\n'
                                 f'👨‍💻  Монтаж - від 30💲\n\n', reply_markup=keyboard)


@dp.callback_query_handler(text_contains='contacts')
async def menu(call: types.CallbackQuery):
    await call.message.edit_text(f'📱Моб.тел - +380975547372\n\n'
                                 f'Instagram - @tolian_ruzhytskyi\n\n'
                                 f'Telegram - @tolian_ruzhytskyi\n\n', reply_markup=keyboard)


@dp.callback_query_handler(text_contains='special_offers')
async def menu(call: types.CallbackQuery):
    await call.message.edit_text(f'Я є прибічником збалансованого обміну\n'
                                 f'послугами або ж товарами, тому якщо\n'
                                 f'у вас є вигідна бартерна пропозиція,\n'
                                 f'то дзвоніть по номеру телефону, що\n'
                                 f'вказаний у меню "Контактні дані 👥"\n', reply_markup=keyboard)


@dp.callback_query_handler(text_contains='reviews')
async def menu(call: types.CallbackQuery):
    await call.message.edit_text('Перейдіть по силці і залишіть коментар', reply_markup=keyboard)


@dp.message_handler(commands=['example'])
async def process_example_command(message: types.Message):
    await message.reply("Виберіть тип відео, приклад якого ви хочите побачити")

    await asyncio.sleep(1)

    await types.ChatActions.upload_video()

    media = types.MediaGroup()

    media.attach_video(types.inputFile('example/video/222.mp4'))

    await message.reply_media_group(media=media)


if __name__ == '__main__':
    executor.start_polling(dp)


