from aiogram.types import Message
from loader import dp
from aiogram.filters import Command

#help commands
@dp.message(Command("help"))
async def help_commands(message:Message):
    await message.answer("🔥 Buyruqlar \n\nBotdan foydalanish uchun '/start' - tugmasini bosing. \n'/about' - Bot haqida qisqacha ma'lumot.\nAdmin bilan bog'lanmoqchi bo'lsangiz \n'/xabar' - Adminga ✉️ xabaringizni yozib qoldiring ! \n'/bot_admin' - Bot admini.")
