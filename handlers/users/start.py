from aiogram.types import Message
from loader import dp,db
from aiogram.filters import CommandStart
from button import menu


@dp.message(CommandStart())
async def start_command(message:Message):
    full_name = message.from_user.full_name
    telegram_id = message.from_user.id
    try:
        db.add_user(full_name=full_name,telegram_id=telegram_id) #foydalanuvchi bazaga qo'shildi      
        await message.answer(text=f"Salom hurmatli {full_name}, Shop botga hush kelibsiz 🤖\nBiz sizga siz hohlagan telefoningizni topishingizga yordam beramiz\nTelefonlarni ko'rish uchun '📱 Phones' tugmasini tanlang.\nBizning joylashuv manzilimizni bilish uchun '📍 Location' tugmasini tanlang.", reply_markup=menu)
    except:
        await message.answer(text=f"Salom hurmatli {full_name}, Shop botga hush kelibsiz 🤖\nBiz sizga siz hohlagan telefoningizni topishingizga yordam beramiz\nTelefonlarni ko'rish uchun '📱 Phones' tugmasini tanlang.\nBizning joylashuv manzilimizni bilish uchun '📍 Location' tugmasini tanlang.", reply_markup=menu)


