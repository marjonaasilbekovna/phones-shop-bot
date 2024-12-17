from aiogram.fsm.state import State, StatesGroup

class Registor(StatesGroup):
    ism = State()
    familiya = State() 
    tel = State()
    email = State()
    viloyat = State()
    phone = State()
    buyurtma = State()