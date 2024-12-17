from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup



# -------------------PHONES---------------------------------------------------------------
phones_inf_mapping = {
    "iphone": "iPhone",
    "samsung": "Samsung",
    "redmi": "Redmi",
    "honor": "Honor",
    "infinix": "Infinix"
}

menu_inline = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="iPhone", callback_data="iphone"), 
            InlineKeyboardButton(text="Samsung", callback_data="samsung")
        ],
        [
            InlineKeyboardButton(text="Redmi", callback_data="redmi"), 
            InlineKeyboardButton(text="Honor", callback_data="honor")
        ],
        [
            InlineKeyboardButton(text="Infinix", callback_data="infinix")           
        ]
    ]
)
# buyurtma berish tugmasi
buyurtma_inline = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Buyurtma berish 🛒", callback_data="buyurtma"), 
        ],
    ]
)

# iPhone modellari uchun keyboard
iphone_models_inline = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="iPhone 11", callback_data="iphone_11"),
            InlineKeyboardButton(text="iPhone 11 Pro", callback_data="iphone_11_pro"),
            InlineKeyboardButton(text="11 Pro max", callback_data="iphone_11_pro_max")          
        ],
        [
            InlineKeyboardButton(text="iPhone 12", callback_data="iphone_12"),
            InlineKeyboardButton(text="iPhone 12 Pro", callback_data="iphone_12_pro"),
            InlineKeyboardButton(text="12 Pro max", callback_data="iphone_12_pro_max")
        ],
        [
            InlineKeyboardButton(text="iPhone 13", callback_data="iphone_13"),
            InlineKeyboardButton(text="iPhone 13 Pro", callback_data="iphone_13_pro"), 
            InlineKeyboardButton(text="13 Pro max", callback_data="iphone_13_pro_max")
        ],
        [
            InlineKeyboardButton(text="iPhone 14", callback_data="iphone_14"),
            InlineKeyboardButton(text="iPhone 14 Pro", callback_data="iphone_14_pro"),
            InlineKeyboardButton(text="14 Pro max", callback_data="iphone_14_pro_max")
        ],
        [

            InlineKeyboardButton(text="iPhone 15", callback_data="iphone_15"),
            InlineKeyboardButton(text="iPhone 15 Pro", callback_data="iphone_15_pro"),
            InlineKeyboardButton(text="15 Pro max", callback_data="iphone_15_pro_max")
        ],
        [
            InlineKeyboardButton(text="iPhone 16", callback_data="iphone_16"),
            InlineKeyboardButton(text="iPhone 16 Pro", callback_data="iphone_16_pro"),
            InlineKeyboardButton(text="16 Pro max", callback_data="iphone_16_pro_max")
        ],
        [
            InlineKeyboardButton(text="🔙 Orqaga", callback_data="back_to_menu")
        ]
    ]
)


# Samsung modellari uchun keyboard
samsung_models_inline = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Samsung S21", callback_data="samsung_s21"),
            InlineKeyboardButton(text="S21 Ultra", callback_data="s21_ultra")
        ],
        [
            InlineKeyboardButton(text="Samsung S22", callback_data="samsung_s22"),
            InlineKeyboardButton(text="S22 Ultra", callback_data="s22_ultra")
        ],
        [
            InlineKeyboardButton(text="Samsung S23", callback_data="samsung_s23"),
            InlineKeyboardButton(text="S23 Ultra", callback_data="s23_ultra")
        ],
        [
            InlineKeyboardButton(text="Samsung S24", callback_data="samsung_s24"),
            InlineKeyboardButton(text="S24 Ultra", callback_data="s24_ultra")
        ],
        [
            InlineKeyboardButton(text="Samsung Note10", callback_data="samsung_note10"),
            InlineKeyboardButton(text="Samsung Note20", callback_data="samsung_note20")
        ],
        [
            InlineKeyboardButton(text="A71", callback_data="a71"),
            InlineKeyboardButton(text="A72", callback_data="a72"),
            InlineKeyboardButton(text="A73", callback_data="a73")
        ],
        [
            InlineKeyboardButton(text="A51", callback_data="a51"),
            InlineKeyboardButton(text="A52", callback_data="a52"),
            InlineKeyboardButton(text="A53", callback_data="a53")
        ],
        [
            InlineKeyboardButton(text="🔙 Orqaga", callback_data="back_to_menu")
        ]
    ]
)


# Redmi modellari uchun keyboard
redmi_models_inline = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Redmi 8", callback_data="redmi_8"),
            InlineKeyboardButton(text="Redmi 8A", callback_data="redmi_8a"),
            InlineKeyboardButton(text="Note 8Pro", callback_data="note_8pro")
        ],
        [
            InlineKeyboardButton(text="Redmi 9A", callback_data="redmi_9a"),
            InlineKeyboardButton(text="Redmi 9s", callback_data="redmi_9s"),
            InlineKeyboardButton(text="Note 9Pro", callback_data="note_9pro")
        ],
        [
            InlineKeyboardButton(text="Redmi 10A", callback_data="redmi_10a"),
            InlineKeyboardButton(text="Note 10", callback_data="note_10"),
            InlineKeyboardButton(text="Note 10Pro", callback_data="note_10pro")
        ],
        [
            InlineKeyboardButton(text="Note 11", callback_data="note_11"),
            InlineKeyboardButton(text="Note 11Pro", callback_data="note_11pro"),
            InlineKeyboardButton(text="Note 11Pro+", callback_data="note_11pro_p")
        ],
        [
            InlineKeyboardButton(text="Redmi 12", callback_data="redmi_12"),
            InlineKeyboardButton(text="Note 12", callback_data="note_12"),
            InlineKeyboardButton(text="Note 12Pro", callback_data="note_12pro")
        ],
        [
            InlineKeyboardButton(text="Redmi 13C", callback_data="13c"),
            InlineKeyboardButton(text="Note 13", callback_data="note_13"),
            InlineKeyboardButton(text="13Pro max", callback_data="note_13pro_max")
        ],
        [
            InlineKeyboardButton(text="🔙 Orqaga", callback_data="back_to_menu")
        ]
    ]
)

# Honor modellari uchun keyboard
honor_models_inline = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Honor x6a", callback_data="honor_x6a"),
            InlineKeyboardButton(text="Honor x6b", callback_data="honor_x6b")
        ],
        [
            InlineKeyboardButton(text="Honor x7a", callback_data="honor_x7a"),
            InlineKeyboardButton(text="Honor x7b", callback_data="honor_x7b")
        ],
        [
            InlineKeyboardButton(text="Honor x8a", callback_data="honor_x8a"),
            InlineKeyboardButton(text="Honor x8b", callback_data="honor_x8b")
        ],
        [
            InlineKeyboardButton(text="Honor x9a", callback_data="honor_x9a"),
            InlineKeyboardButton(text="Honor x9b", callback_data="honor_x9b")
        ],
        [
            InlineKeyboardButton(text="Honor x10a", callback_data="honor_x10a"),
            InlineKeyboardButton(text="Honor x10b", callback_data="honor_x10b")
        ],
        [
            InlineKeyboardButton(text="🔙 Orqaga", callback_data="back_to_menu")
        ]
    ]
)


# Infinix modellari uchun keyboard
infinix_models_inline = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Smart 6", callback_data="smart6"),
            InlineKeyboardButton(text="Smart 7", callback_data="smart7")
        ],
        [
            InlineKeyboardButton(text="Smart 8", callback_data="smart8"),
            InlineKeyboardButton(text="Smart 9", callback_data="smart9")
        ],
        [
            InlineKeyboardButton(text="Hot 6", callback_data="hot6"),  
            InlineKeyboardButton(text="Hot 7", callback_data="hot7")
        ],
        [
            InlineKeyboardButton(text="Hot 8", callback_data="hot8"),
            InlineKeyboardButton(text="Hot 9", callback_data="hot9")
        ],
        [
            InlineKeyboardButton(text="🔙 Orqaga", callback_data="back_to_menu")
        ]
    ]
)

# iphone_phones_inf_mapping = {
#     "iphone_11": "iPhone 11",
#     "iphone_11_pro": "iPhone 11 Pro",
#     "iphone_11_pro_max": "11 Pro max",
#     "iphone_12": "iPhone 12",
#     "iphone_12_pro": "iPhone 12 Pro",
#     "iphone_12_pro_max": "12 Pro max",
#     "iphone_13": "iPhone 13",
#     "iphone_13_pro": "iPhone 13 Pro",
#     "iphone_13_pro_max": "13 Pro max",
#     "iphone_14": "iPhone 14",
#     "iphone_14_pro": "iPhone 14 Pro",
#     "iphone_14_pro_max": "14 Pro max",
#     "iphone_15": "iPhone 15",
#     "iphone_15_pro": "iPhone 15 Pro",
#     "iphone_15_pro_max": "15 Pro max",
#     "iphone_16": "iPhone 16",
#     "iphone_16_pro": "iPhone 16 Pro",
#     "iphone_16_pro_max": "16 Pro max"
#     }

# samsung_phones_inf_mapping = {
#     "samsung_s21": "Samsung S21",
#     "s21_ultra": "s21 Ultra",
#     "samsung_s22": "amsung S22",
#     "s22_ultra": "S22 Ultra",
#     "samsung_s23": "Samsung S23",
#     "s23_ultra": "S23 Ultra",
#     "samsung_s24": "Samsung S24",
#     "s24_ultra": "S24 Ultra",
#     "samsung_note10": "Samsung Note10",
#     "samsung_note20": "Samsung Note20",
#     "a71": "A71",
#     "a72": "A72",
#     "a73": "A73",
#     "a51": "A51",
#     "a52": "A52",
#     "a53": "A53"
# }

# redmi_phones_inf_mapping = {
#     "redmi_8": "Redmi 8",
#     "redmi_8a": "Redmi 8A",
#     "note_8pro": "Note 8Pro",
#     "redmi_9a": "Redmi 9",
#     "redmi_9s": "Redmi 9s",
#     "note_9pro": "Note 9Pro",
#     "redmi_10a": "Redmi 10A",
#     "note_10pro": "Note 10Pro",
#     "note_11": "Note 11",
#     "note_11pro": "Note 11Pro",
#     "note_11pro_p": "Note 11Pro+",
#     "redmi_12": "Redmi 12",
#     "note_12": "Note 12",
#     "note_12pro": "Note 12Pro",
#     "13c": "Redmi 13C",
#     "note_13c": "Note 13",
#     "note_13pro_max": "13 Pro max"
# }

# honor_phones_inf_mapping = {
#     "honor_x6a": "Honor x6a",
#     "honor_x6b": "Honor x6b",
#     "honor_x7a": "Honor x7a",
#     "honor_x7b": "Honor x7b",
#     "honor_x8a": "Honor x8a",
#     "honor_x8b": "Honor x8b",
#     "honor_x9a": "Honor x9a",
#     "honor_x9b": "Honor x9b",
#     "honor_x10a": "Honor x10a",
#     "honor_x10b": "Honor x10b"
# }

# infinix_phones_inf_mapping = {
#     "smart6": "Smart 6",
#     "smart7": "Smart 7",
#     "smart8": "Smart 8",
#     "smart9": "Smart 9",
#     "hot6": "Hot 6",
#     "hot7": "Hot 7",
#     "hot8": "Hot 8",
#     "hot9": "Hot 9",
#     "hot10": "Hot 10"
# }