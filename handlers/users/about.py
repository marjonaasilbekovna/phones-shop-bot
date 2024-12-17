from aiogram.types import Message
from loader import dp
from aiogram.filters import Command

#about commands
@dp.message(Command("about"))
async def about_button(message: Message):
    text = "Hurmatli foydalanuvchi 'Online telefon xarid qilish' botiga hush kelinsiz.Siz bu bot orqali istalgan turdagi telefoningizni oson topishingiz mumkin  bo'ladi.\nBotga '/start' tugmasini bosib o'zingizga kerakli telefonnni tanlang va buyurtma bering.\nBuyurtmangiz sizga tez va ishonchli yetib boradi.\n\nBU bot 'Sifatedu' o'quv markazi tomonidan yaratilgan.  "
    pic_url = "https://i.pinimg.com/originals/40/a9/c3/40a9c329dba2278c9775798067ebae2d.jpg"
    await message.answer_photo(pic_url, caption=text)

