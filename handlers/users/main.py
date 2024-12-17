from aiogram import F
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from reg_states import Registor
from button import menu, send_contact
from baza_bot import iphone_info, samsung_info, redmi_info, infinix_info, honor_info
from inline_button import menu_inline, iphone_models_inline, samsung_models_inline, redmi_models_inline, honor_models_inline, infinix_models_inline, buyurtma_inline
from loader import dp,bot,ADMINS



@dp.callback_query(lambda c: c.data == 'buyurtma')  # Callback so'rovlari uchun to'g'ri handler
async def buyurtma_button(callback_query: CallbackQuery, state: FSMContext):
    # Callbackni tasdiqlash
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, f"Hurmatli mijoz...\nTelefonga buyurtma berish uchun avval ro'yxatdan o'ting!\nIsmingizni kiriting: ")
    await state.set_state(Registor.ism)



@dp.message(F.text=="📍 Location")
async def location(message: Message):
    text = "Bizning savdo markazimizning lokatsiyasi!"
    lat = 40.102607
    lon = 65.37462
    await message.answer_location(lat, lon)
    await message.answer(text)

# latitude bilan longitude olish kodi 
# @dp.message(F.location)
# async def location(message: Message):
#     lat = message.location.latitude
#     lon = message.location.longitude

#     text = f"latitude:<code>{lat}</code>\n"
#     text += f"longitude:<code>{lon}</code>"

#     await message.answer(text, parse_mode="html")




# Telefonlar ro'yxatini ko'rsatish


# Phones tugmasi
@dp.message(F.text == "📱 Phones")
async def phones(message: Message):
    await message.answer("Telefonlar ro'yxati:", reply_markup=menu_inline)

#iPhone modellari
@dp.callback_query(lambda c: c.data == 'iphone')
async def show_iphone_models(callback_query: CallbackQuery):
    await callback_query.message.delete()
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, "To'liq ma'lumot uchun iPhone telefonlari turidan birini tanlang 📱", reply_markup=iphone_models_inline)

# Kiritilgan modellardan tugmalar matni orqali tanlash
@dp.callback_query(lambda callback: callback.data in iphone_info.keys())
async def iphone_infos(callback_query: CallbackQuery, state: FSMContext):
    await callback_query.message.delete()
    selected_iphone = callback_query.data
    info = iphone_info.get(selected_iphone)

    model_name = selected_iphone.replace("_", " ").title().replace("Pro Max", "Pro Max")
    print(model_name)
    if info:
        # Telefon ma'lumotlari
        photo = info["rasm"]
        rang = info["rang"]
        xotira = info["xotira"]
        narx = info["narx"]
       
        text = f"Telefon nomi: {model_name}\nNarxi: {narx} $\nRangi: {rang}\nXotirasi: {xotira}"

        # Telefon nomini state ga saqlash
        await state.update_data(phone=model_name)

        # Telefon ma'lumotlarini yuborish
        await bot.send_photo(callback_query.from_user.id, photo, caption=text, reply_markup=buyurtma_inline)
    else:
        await bot.send_message(callback_query.from_user.id, "Telefon ma'lumotlari topilmadi 😢")

        

@dp.callback_query(lambda callback: callback.data == "buyurtma")
async def start_registration(callback_query: CallbackQuery, state: FSMContext):
    data = await state.get_data() 
    phone = data.get("phone")

# Samsung modellari
@dp.callback_query(lambda c: c.data == 'samsung')
async def show_samsung_models(callback_query: CallbackQuery):
    await callback_query.message.delete()
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, "To'liq ma'lumot uchun Samsung telefonlari turidan birini tanlang 📱", reply_markup=samsung_models_inline)

@dp.callback_query(lambda callback: callback.data in samsung_info.keys())
async def samsung_infos(callback_query: CallbackQuery, state: FSMContext):
    await callback_query.message.delete()
    selected_model = callback_query.data
    info = samsung_info.get(selected_model)


    if info:
        photo = info["rasm"]
        rang = info["rang"]
        xotira = info["xotira"]
        narx = info["narx"]
        # Model nomini formatlash: harflar katta bo'lishi uchun
        model_name = selected_model.replace("_", " ").title().replace("S", "S").replace("Note", "Note ")
        print(model_name)
        text = f"Telefon nomi: {model_name}\nNarxi: {narx} $\nRangi: {rang}\nXotirasi: {xotira}"
        # model_name - state da saqlab olish kerak

        await state.update_data(phone=model_name)

        await bot.send_photo(callback_query.from_user.id, photo, caption=text, reply_markup=buyurtma_inline)
    else:
        await bot.send_message(callback_query.from_user.id, "Telefon ma'lumotlari topilmadi 😢")


# Redmi modellari
@dp.callback_query(lambda c: c.data == 'redmi')
async def show_redmi_models(callback_query: CallbackQuery):
    await callback_query.message.delete()
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, "Tuliq malumot olish uchun Redmi telefonlari turidan birini tanlang 📱", reply_markup=redmi_models_inline)

@dp.callback_query(lambda callback: callback.data in redmi_info.keys())
async def redmi_infos(callback_query: CallbackQuery, state: FSMContext):
    await callback_query.message.delete()
    selected_redmi = callback_query.data
    info = redmi_info.get(selected_redmi)

    if info:
        photo = info["rasm"]
        rang = info["rang"]
        xotira = info["xotira"]
        narx = info["narx"]
        # Tugmada Redmi modellarini katta harf bilan ko'rsatamiz
        model_name = selected_redmi.replace("_", " ").title()
        print(model_name)
        text = f"Telefon nomi: {model_name}\nNarxi: {narx} $\nRangi: {rang}\nXotirasi: {xotira}"

        await state.update_data(phone=model_name)

        await bot.send_photo(callback_query.from_user.id, photo, caption=text, reply_markup=buyurtma_inline)
    else:
        await bot.send_message(callback_query.from_user.id, "Telefon ma'lumotlari topilmadi 😢")

# Honor modellari
@dp.callback_query(lambda c: c.data == 'honor')
async def show_honor_models(callback_query: CallbackQuery):
    await callback_query.message.delete()
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, "Tuliq malumot olish uchun Honor telefonlari turidan birini tanlang 📱", reply_markup=honor_models_inline)

@dp.callback_query(lambda callback: callback.data in honor_info.keys())
async def honor_infos(callback_query: CallbackQuery, state: FSMContext):
    await callback_query.message.delete()
    selected_honor = callback_query.data
    info = honor_info.get(selected_honor)

    if info:
        photo = info["rasm"]
        rang = info["rang"]
        xotira = info["xotira"]
        narx = info["narx"]
        # Tugmada Honor modellarini katta harf bilan ko'rsatamiz
        model_name = selected_honor.replace("_", " ").title()
        print(model_name)
        text = f"Telefon nomi: {model_name}\nNarxi: {narx} $\nRangi: {rang}\nXotirasi: {xotira}"

        await state.update_data(phone=model_name)

        await bot.send_photo(callback_query.from_user.id, photo, caption=text, reply_markup=buyurtma_inline)
    else:
        await bot.send_message(callback_query.from_user.id, "Telefon ma'lumotlari topilmadi 😢")

# Infinix modellari
@dp.callback_query(lambda c: c.data == 'infinix')
async def show_infinix_models(callback_query: CallbackQuery):
    await callback_query.message.delete()
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, "Tuliq malumot olish uchun Infinix telefonlari turidan birini tanlang 📱", reply_markup=infinix_models_inline)

@dp.callback_query(lambda callback: callback.data in infinix_info.keys())
async def infinix_infos(callback_query: CallbackQuery, state: FSMContext):
    await callback_query.message.delete()
    selected_infinix = callback_query.data
    info = infinix_info.get(selected_infinix)

    if info:
        photo = info["rasm"]
        rang = info["rang"]
        xotira = info["xotira"]
        narx = info["narx"]
        # Tugmada Infinix modellarini katta harf bilan ko'rsatamiz
        model_name = selected_infinix.replace("_", " ").title()
        print(model_name)
        text = f"Telefon nomi: {model_name}\nNarxi: {narx} $\nRangi: {rang}\nXotirasi: {xotira}"

        await state.update_data(phone=model_name)

        await bot.send_photo(callback_query.from_user.id, photo, caption=text, reply_markup=buyurtma_inline)
    else:
        await bot.send_message(callback_query.from_user.id, "Telefon ma'lumotlari topilmadi 😢")



# Orqaga tugmasini telefon turlarida ishlatish
@dp.callback_query(lambda c: c.data == 'back_to_menu')
async def back_to_menu(callback_query: CallbackQuery):
    await callback_query.message.delete()
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, "Telefonlar ro'yxati:", reply_markup=menu_inline)

# First_name
@dp.message(F.text, Registor.ism)
async def register_ism(message: Message, state:FSMContext):
    ism = message.text
    if ism.isalpha(): 
        await state.update_data(name = ism)
        await state.set_state(Registor.familiya)
        await message.answer("Familiyani kiriting")
    else:
        await message.delete()
        await message.answer("Ismingizni tug'ri kiriting ❗️")

# Agar kiritilgan qiymat text bo'lmasa ushbu kod ishga tushadi
@dp.message(Registor.ism)
async def register_ism_del(message:Message, state:FSMContext):
    await message.delete()
    await message.answer(text= "Ismimgizni to'g'ri kiriting ❗️")

# end First_name

@dp.message(F.text, Registor.familiya)
async def register_familiya(message: Message, state:FSMContext):
    familiya = message.text  
    if familiya.isalpha():
        await state.update_data(surname = familiya)
        await state.set_state(Registor.tel)
        await message.answer("Telefon raqimgizni kiriting yoki  'Kontakt yuborish ☎️'  tugmasi orqali raqamingizni kiriting :", reply_markup=send_contact)
    else:
        await message.delete()
        await message.answer("Familyangizni tug'ri kiriting ❗️")


@dp.message(Registor.familiya)
async def register_familiya_del(message: Message, state:FSMContext):
    await message.delete()
    await message.answer(text= "Familiyangizni tug'ri kiriting ❗️")



# Phone_number  F.contact | F.text, SingUp.tel
@dp.message(F.contact | F.text.regexp( r"^(\+998|998)[0-9]{9}$"), Registor.tel)
async def register_tel(message: Message, state:FSMContext):

    if message.contact:
        tel = message.contact.phone_number 
    else:
        tel = message.text

    await state.update_data(tel = tel)
    await state.set_state(Registor.email)
    await message.answer("Emailingizni kiriting :")

@dp.message(Registor.tel)
async def register_tel_del(message:Message, state:FSMContext):
    await message.delete()
    await message.answer(text= "Telefon raqamni to'g'ri kiriting ❗️")

# end Phone_number

@dp.message(F.text.regexp(r"[^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+"), Registor.email)
async def register_email(message: Message, state:FSMContext):
    email = message.text
    await state.update_data(email = email)
    await state.set_state(Registor.viloyat)
    await message.answer("Yashash manzilingizni kiriting :", reply_markup=None)

@dp.message(F.text, Registor.viloyat)
async def register_tuman(message: Message, state:FSMContext):
    data = await state.get_data()
    phone = data.get("phone")
    print(phone)
    ism = data.get("name")
    familiya = data.get("surname")
    tel = data.get("tel")
    email = data.get("email")
    viloyat = message.text

    username = message.from_user.username
    full_name = message.from_user.full_name
    text = f"Ism : {ism} \nFamiliya : {familiya} \nTel : {tel} \nEmail: {email}\nManzil: {viloyat} \n\nBuyurtma : {phone}\n\nUsername ;   @{username}\nFull name ;   {full_name}"
    await message.answer(f"Siz ro'yxatdan muvaffaqqiyatli o'tdingiz 👍🏻😀.\nVa siz  '{phone}'  telefonini buyurtma qildingiz.\n\nAdmin siz bilan bog'lanishini kuting.\nBuyurtmangiz yaqin orada yetib boradi 😀", reply_markup=menu)

    await bot.send_message(chat_id= 7241341727, text=text)
    await state.clear()

@dp.message(Registor.email)
async def register_email_del(message: Message, state:FSMContext):
    await message.delete() 
    await message.answer(text= "Emailingizni tug'ri kiriting ❗️")


@dp.message(F.text=="Orqaga qaytish 🔙")
async def back_button(message: Message):
    text = "Menu"
    await message.answer(text, reply_markup=menu)