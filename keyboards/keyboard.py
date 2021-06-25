from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


"""Стартове меню"""
keyboard = InlineKeyboardMarkup()
services = InlineKeyboardButton(text='Види послуг 📋', callback_data="services")
price = InlineKeyboardButton(text='Прайс-лист 💵', callback_data="price")
contacts = InlineKeyboardButton(text='Контактні дані 👥', callback_data="contacts")
special_offers = InlineKeyboardButton(text='Особливі пропозиції 🤝', callback_data="special_offers")
reviews = InlineKeyboardButton(text='Відгуки 🗣', callback_data="reviews")
keyboard.add(services, price, contacts, special_offers, reviews)


"""Меню прикладів відео"""
keyboard_for_example = InlineKeyboardMarkup()
klip = InlineKeyboardButton(text='Кліп 🎬', callback_data="klip")
fashion = InlineKeyboardButton(text='Fashion 👗', callback_data="fashion")
promotional_videos = InlineKeyboardButton(text='Рекламні відео 📢', callback_data="promotional_videos")
wedding_videos = InlineKeyboardButton(text='Весільні відео 💍', callback_data="wedding_videos")
love_story = InlineKeyboardButton(text='Love story 💏', callback_data="love_story")
aerovideo = InlineKeyboardButton(text='Аерозйомка ✈', callback_data="aerovideo")
video_editing = InlineKeyboardButton(text='Монтаж 👨‍💻', callback_data="video_edition")
keyboard_for_example.add(klip, fashion, promotional_videos, wedding_videos, love_story, aerovideo, video_editing)