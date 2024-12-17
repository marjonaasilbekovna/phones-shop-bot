from aiogram.types import KeyboardButton,ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder

send_contact = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Kontakt yuborish ☎️", request_contact=True)]
    ],
    resize_keyboard=True,
)

location_button = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="📍 joylashuvni yuborish", request_location=True)]
    ],
    resize_keyboard=True,
)


menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="📱 Phones"), KeyboardButton(text="📍 Location")]
    ],
    resize_keyboard=True,
    input_field_placeholder="Tugmalardan birini tanlang ..."
)



