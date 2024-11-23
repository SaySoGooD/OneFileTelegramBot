from aiogram.fsm.state import StatesGroup, State


class EditFile(StatesGroup):
    upload = State()


class EditMessage(StatesGroup):
    number = State()
    text = State()


class RandomMSG(StatesGroup):
    text = State()