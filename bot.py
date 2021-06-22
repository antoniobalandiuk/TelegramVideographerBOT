import asyncio

from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.exceptions import MessageNotModified
from config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

keyboard = InlineKeyboardMarkup()
services = InlineKeyboardButton(text='Види послуг 📋', callback_data="services")
price = InlineKeyboardButton(text='Прайс-лист 💵', callback_data="price")
contacts = InlineKeyboardButton(text='Контактні дані 👥', callback_data="contacts")
special_offers = InlineKeyboardButton(text='Особливі пропозиції 🤝', callback_data="special_offers")
reviews = InlineKeyboardButton(text='Відгуки 🗣', callback_data="reviews")
keyboard.add(services, price, contacts, special_offers, reviews)


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply(f'Привіт! Я - відеомейкер з почуттям стилю!🎞🎥\n\n'
                        f'Я – Анатолій Ружицький, мені 16 років👦. \"16?! Та ти обманюєш!\" - часто чую такі реакції з боку своїх клієнтів, які вподальшому говорять: \"Вірний своїй справі, вірний своїм переконанням, бомбезний оператор, в якого все ще попереду!\n\n'
                        f'Моя робота — створити приємні спогади, відтворити атмосферу подій на природі🛤, у місті🌇 чи студії🎼, запам`ятати усі емоції в кадрах.',
                        reply_markup=keyboard)


@dp.callback_query_handler(text_contains='services')
async def services(call: types.CallbackQuery):
    await call.message.edit_text(f'Тут будуть послуги, моделі камер та дрону', reply_markup=keyboard)


@dp.callback_query_handler(text_contains='price')
async def price(call: types.CallbackQuery):
    await call.message.edit_text(f'🎬  Кліпи - від 200💲\n\n'
                                 f'👗  Fashion - від 100💲\n\n'
                                 f'📢  Рекламні відео - від 100💲\n\n'
                                 f'💍  Весільні фільми - є кілька пакетів, залежно від кількості знімальних годин, камер та наявності аерозйомки\n\n'
                                 f'💏  Love Story - 100💲\n\n'
                                 f'✈  Аерозйомка - від 50💲\n\n'
                                 f'👨‍💻  Монтаж - від 30💲\n\n', reply_markup=keyboard)


@dp.callback_query_handler(text_contains='contacts')
async def contacts(call: types.CallbackQuery):
    await call.message.edit_text(f'📱Моб.тел - +380975547372\n\n'
                                 f'📸Instagram - @tolian_ruzhytskyi\n\n'
                                 f'✉Telegram - @tolian_ruzhytskyi\n\n', reply_markup=keyboard)


@dp.callback_query_handler(text_contains='special_offers')
async def special_offers(call: types.CallbackQuery):
    await call.message.edit_text(f'Я є прибічником збалансованого обміну\n'
                                 f'послугами або ж товарами, тому якщо\n'
                                 f'у вас є вигідна бартерна пропозиція,\n'
                                 f'то дзвоніть по номеру телефону, що\n'
                                 f'вказаний у меню "Контактні дані 👥"\n', reply_markup=keyboard)


@dp.callback_query_handler(text_contains='reviews')
async def reviews(call: types.CallbackQuery):
    await call.message.edit_text('Перейдіть по силці і залишіть коментар', reply_markup=keyboard)


keyboard_for_example = InlineKeyboardMarkup()
klip = InlineKeyboardButton(text='Кліп 🎬', callback_data="klip")
fashion = InlineKeyboardButton(text='Fashion 👗', callback_data="fashion")
promotional_videos = InlineKeyboardButton(text='Рекламні відео 📢', callback_data="promotional_videos")
wedding_videos = InlineKeyboardButton(text='Весільні відео 💍', callback_data="wedding_videos")
love_story = InlineKeyboardButton(text='Love story 💏', callback_data="love_story")
aerovideo = InlineKeyboardButton(text='Аерозйомка ✈', callback_data="aerovideo")
video_editing = InlineKeyboardButton(text='Монтаж 👨‍💻', callback_data="video_edition")
keyboard_for_example.add(klip, fashion, promotional_videos, wedding_videos, love_story, aerovideo, video_editing)


@dp.message_handler(commands=['example'])
async def message_before_example(message: types.Message):
    await message.reply('Ви увыйшли в меню "/example"\n'
                        'Натискаючи на кнопки під цим текстом ви вибираєте\n'
                        'тип відео, яке ви хочете переглянути', reply_markup=keyboard_for_example)


@dp.callback_query_handler(text_contains='klip')
async def clip(call: types.CallbackQuery):
    await asyncio.sleep(1)
    await types.ChatActions.upload_video()
    media = types.MediaGroup()
    media.attach_video(types.InputFile('example/video/🔥OVERWATCH FUNNY MOMENTS #3 ОВЕРВОТЧ #SHORTS ► СМЕШНЫЕ МОМЕНТЫ ОВЕРВАЧ _ ШОРТС _ КОРОТКИЕ ВИДЕО ЮТУБ.mp4'))
    await call.message.reply_media_group(media=media)


@dp.callback_query_handler(text_contains='fashion')
async def fashion(call: types.CallbackQuery):
    await asyncio.sleep(1)
    await types.ChatActions.upload_video()
    media = types.MediaGroup()
    media.attach_video(types.InputFile('example/video/🔥OVERWATCH FUNNY MOMENTS #3 ОВЕРВОТЧ #SHORTS ► СМЕШНЫЕ МОМЕНТЫ ОВЕРВАЧ _ ШОРТС _ КОРОТКИЕ ВИДЕО ЮТУБ.mp4'))
    await call.message.reply_media_group(media=media)


@dp.callback_query_handler(text_contains='promotional_videos')
async def promotional_videos(call: types.CallbackQuery):
    await asyncio.sleep(1)
    await types.ChatActions.upload_video()
    media = types.MediaGroup()
    media.attach_video(types.InputFile('example/video/🔥OVERWATCH FUNNY MOMENTS #3 ОВЕРВОТЧ #SHORTS ► СМЕШНЫЕ МОМЕНТЫ ОВЕРВАЧ _ ШОРТС _ КОРОТКИЕ ВИДЕО ЮТУБ.mp4'))
    await call.message.reply_media_group(media=media)


@dp.callback_query_handler(text_contains='wedding_videos')
async def promotional_videos(call: types.CallbackQuery):
    await asyncio.sleep(1)
    await types.ChatActions.upload_video()
    media = types.MediaGroup()
    media.attach_video(types.InputFile('example/video/🔥OVERWATCH FUNNY MOMENTS #3 ОВЕРВОТЧ #SHORTS ► СМЕШНЫЕ МОМЕНТЫ ОВЕРВАЧ _ ШОРТС _ КОРОТКИЕ ВИДЕО ЮТУБ.mp4'))
    await call.message.reply_media_group(media=media)


@dp.callback_query_handler(text_contains='love_story')
async def promotional_videos(call: types.CallbackQuery):
    await asyncio.sleep(1)
    await types.ChatActions.upload_video()
    media = types.MediaGroup()
    media.attach_video(types.InputFile('example/video/🔥OVERWATCH FUNNY MOMENTS #3 ОВЕРВОТЧ #SHORTS ► СМЕШНЫЕ МОМЕНТЫ ОВЕРВАЧ _ ШОРТС _ КОРОТКИЕ ВИДЕО ЮТУБ.mp4'))
    await call.message.reply_media_group(media=media)


@dp.callback_query_handler(text_contains='love_story')
async def promotional_videos(call: types.CallbackQuery):
    await asyncio.sleep(1)
    await types.ChatActions.upload_video()
    media = types.MediaGroup()
    media.attach_video(types.InputFile('example/video/🔥OVERWATCH FUNNY MOMENTS #3 ОВЕРВОТЧ #SHORTS ► СМЕШНЫЕ МОМЕНТЫ ОВЕРВАЧ _ ШОРТС _ КОРОТКИЕ ВИДЕО ЮТУБ.mp4'))
    await call.message.reply_media_group(media=media)


@dp.callback_query_handler(text_contains='aerovideo')
async def promotional_videos(call: types.CallbackQuery):
    await asyncio.sleep(1)
    await types.ChatActions.upload_video()
    media = types.MediaGroup()
    media.attach_video(types.InputFile('example/video/🔥OVERWATCH FUNNY MOMENTS #3 ОВЕРВОТЧ #SHORTS ► СМЕШНЫЕ МОМЕНТЫ ОВЕРВАЧ _ ШОРТС _ КОРОТКИЕ ВИДЕО ЮТУБ.mp4'))
    await call.message.reply_media_group(media=media)


@dp.callback_query_handler(text_contains='video_edition')
async def promotional_videos(call: types.CallbackQuery):
    await asyncio.sleep(1)
    await types.ChatActions.upload_video()
    media = types.MediaGroup()
    media.attach_video(types.InputFile('example/video/🔥OVERWATCH FUNNY MOMENTS #3 ОВЕРВОТЧ #SHORTS ► СМЕШНЫЕ МОМЕНТЫ ОВЕРВАЧ _ ШОРТС _ КОРОТКИЕ ВИДЕО ЮТУБ.mp4'))
    await call.message.reply_media_group(media=media)


@dp.errors_handler(exception=MessageNotModified)
async def message_not_modified_handler(update, error):
    return True

"""Це надсилає відео в бота"""
# @dp.message_handler(text_contains='example_video')
# async def process_example_command(call: types.CallbackQuery):
#     await call.message.edit_text('Виберіть тип відео, приклад якого ви хочите побачити', reply_markup=keyboard)
#
#     await asyncio.sleep(1)
#
#     await types.ChatActions.upload_video()
#
#     media = types.MediaGroup()
#
#     media.attach_video(types.InputFile('example/video/advert.mp4'))
#
#     await call.message.reply_media_group(media=media)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)


