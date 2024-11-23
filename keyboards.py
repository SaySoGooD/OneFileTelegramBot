from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton


async def admin_kb():
    return ReplyKeyboardMarkup(keyboard=[
        [
            KeyboardButton(
                text="Изменить сообщение")
        ],
        [
            KeyboardButton(
                text="Изменить файл")
        ]
    ], resize_keyboard=True)


async def cancel_state_kb():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text='Отмена',
                    callback_data='cancel_state'
                )
            ]
        ]
    )