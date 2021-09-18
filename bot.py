import asyncio

from aiogram import types
from aiogram.utils import executor
from aiogram.utils.exceptions import MessageNotModified

from loader import dp
from keyboards.keyboard import keyboard, keyboard_for_example


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply(f'Тут ви знайдете всю необхідну вам інформацію '
                        f'про послуги RA Production. А коли ви переглянете '
                        f'всі пункти меню, що вас цікавлять, то натискайте '
                        f'кнопку "Контактні дані 👥" та звертайтесь до мене '
                        f'за найяскравішими кадрами у вашому житті', reply_markup=keyboard)


# async def showreel(call: types.CallbackQuery):
#     await asyncio.sleep(1)
#     await types.ChatActions.upload_video()
#     media = types.MediaGroup
#     media.attach_video(types.InputFile('example/video/wedding.mp4'))
#     await call.message.reply_media_group(media=media)


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
    await call.message.edit_text(f'Будь ласка, перейдіть по посиланню - \n'
                                 f'та залишіть заяву для бартерного обміну послугами\n'
                                 f'https://forms.gle/Jv79qnfyQCXVECMi6\n', reply_markup=keyboard)


@dp.callback_query_handler(text_contains='reviews')
async def reviews(call: types.CallbackQuery):
    await call.message.edit_text('Перейдіть по силці і залишіть коментар\n'
                                 'https://forms.gle/GXw4s2jXozshadYk8', reply_markup=keyboard)


@dp.message_handler(commands=['example'])
async def message_before_example(message: types.Message):
    await message.reply('Увага!!! Відео в даних прикладах подані уривками\n'
                        'Повні версії ви зможете глянути за посиланням\n'
                        'https://m.youtube.com/channel/UCBCrDx6CdQ0BYelhH99IkIg\n'
                        'НАЖМІТЬ НА КНОПКУ І ЧЕКАЙТЕ ЗАВАНТАЖЕННЯ ВІДЕО6', reply_markup=keyboard_for_example)


@dp.callback_query_handler(text_contains='klip')
async def clip(call: types.CallbackQuery):
    await asyncio.sleep(1)
    await types.ChatActions.upload_video()
    media = types.MediaGroup()
    media.attach_video(types.InputFile('example/video/KLIP.mp4'))
    await call.message.reply_media_group(media=media)


@dp.callback_query_handler(text_contains='fashion')
async def fashion(call: types.CallbackQuery):
    await asyncio.sleep(1)
    await types.ChatActions.upload_video()
    media = types.MediaGroup()
    media.attach_video(types.InputFile('example/video/advert_Trim.mp4'))
    await call.message.reply_media_group(media=media)


@dp.callback_query_handler(text_contains='promotional_videos')
async def promotional_videos(call: types.CallbackQuery):
    await asyncio.sleep(1)
    await types.ChatActions.upload_video()
    media = types.MediaGroup()
    media.attach_video(types.InputFile('example/video/Promo_1.mp4'))
    await call.message.reply_media_group(media=media)


@dp.callback_query_handler(text_contains='wedding_videos')
async def wedding_videos(call: types.CallbackQuery):
    await asyncio.sleep(1)
    await types.ChatActions.upload_video()
    media = types.MediaGroup()
    media.attach_video(types.InputFile('example/video/wedding.mp4'))
    await call.message.reply_media_group(media=media)


@dp.callback_query_handler(text_contains='love_story')
async def love_story(call: types.CallbackQuery):
    await asyncio.sleep(1)
    await types.ChatActions.upload_video()
    media = types.MediaGroup()
    media.attach_video(types.InputFile('example/video/love_story.mp4'))
    await call.message.reply_media_group(media=media)


@dp.callback_query_handler(text_contains='aerovideo')
async def aerovideo(call: types.CallbackQuery):
    await asyncio.sleep(1)
    await types.ChatActions.upload_video()
    media = types.MediaGroup()
    media.attach_video(types.InputFile('example/video/story_drone.mp4'))
    await call.message.reply_media_group(media=media)


@dp.errors_handler(exception=MessageNotModified)
async def message_not_modified_handler(update, error):
    return True


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)


