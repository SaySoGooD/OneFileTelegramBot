import os

from aiogram import Router, F, Bot
from aiogram.filters import CommandStart, Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, FSInputFile, CallbackQuery

from config import ADMINS, msgs
from keyboards import admin_kb, cancel_state_kb
from middlewares import LoggingBot, CheckAdmin
from states import EditFile, EditMessage, RandomMSG

user_router = Router()
user_router.message.middleware(LoggingBot())
user_router.callback_query.middleware(LoggingBot())
admin_router = Router()
admin_router.message.middleware(CheckAdmin())
admin_router.callback_query.middleware(CheckAdmin())


async def save_file_id(file_id):
    with open("file_id.txt", "w") as file:
        file.write(file_id)


async def get_saved_file_id():
    try:
        with open("file_id.txt", "r") as file:
            return file.read().strip()
    except Exception as e:
        print(e)
        return None


async def update_message_in_file(new_message, message_index):
    with open("msg.txt", 'r', encoding='utf-8') as f:
        messages = f.readlines()
    if 0 <= message_index < len(messages):
        messages[message_index] = new_message + '\n'
        with open("msg.txt", 'w', encoding='utf-8') as f:
            f.writelines(messages)
        print(msgs[str(message_index+1)])
        msgs[str(message_index+1)] = new_message
        print("Сообщение успешно обновлено.")
        print(msgs[str(message_index+1)])
    else:
        print("Неверный индекс сообщения.")


@user_router.message(Command('start'))
async def start_msg(msg: Message, state:FSMContext):
    await msg.answer(msgs["1"])
    await msg.answer(msgs["2"])
    await state.set_state(RandomMSG.text)


@user_router.message(RandomMSG.text)
async def send_file(msg: Message, state: FSMContext):
    file_id = await get_saved_file_id()
    if file_id:
        await msg.answer_document(document=file_id,
                                  caption=msgs["3"])
    else:
        await msg.answer("Файл не найден.")
    await state.clear()


@admin_router.message(Command('admin'))
async def admin_panel(msg: Message):
    await msg.answer(text='Админ панель активирована',
                     reply_markup=await admin_kb())


@admin_router.message(F.text == 'Изменить файл')
async def edit_file(msg: Message, state: FSMContext):
    msg_to_delete = await msg.answer(text='Отправьте файл',
                                     reply_markup=await cancel_state_kb())
    await state.update_data(msg_to_delete=msg_to_delete.message_id)
    try:
        await msg.delete()
    except Exception as e:
        await msg.answer(f'Возникла ошибка при удалении сообщения: {e}')
        pass
    await state.set_state(EditFile.upload)


@admin_router.callback_query(F.data == 'cancel_state')
async def cancel_state(cb: CallbackQuery, state: FSMContext):
    await state.clear()
    try:
        await cb.message.delete()
    except Exception as e:
        await cb.answer(f'Возникла ошибка при удалении сообщения: {e}')
        pass


@admin_router.message(EditFile.upload)
async def upload_new_file(msg: Message, state: FSMContext, bot: Bot):
    data = await state.get_data()
    doc = msg.document
    if doc:
        file_id = doc.file_id
        await save_file_id(file_id)
        await msg.answer(f'Файл успешно загружен!\n\n'
                         f'Eго айди: {file_id}')
        await state.clear()
    else:
        msg_to_delete = await msg.answer('Файл не обнаружен, попробуйте ещё')
        await state.update_data(msg_to_delete=msg_to_delete.message_id)
    await bot.delete_message(chat_id=msg.chat.id, message_id=int(data['msg_to_delete']))


@admin_router.message(F.text == 'Изменить сообщение')
async def edit_file(msg: Message, state: FSMContext):
    msg_to_delete = await msg.answer(text='Отправьте номер сообщения\n\n'
                                          'Сообщение 1 и 2 отправляются в начале\n'
                                          'Сообщение 3 отправляется вместе с файлом\n',
                                     reply_markup=await cancel_state_kb())
    await state.update_data(msg_to_delete=msg_to_delete.message_id)
    try:
        await msg.delete()
    except Exception as e:
        await msg.answer(f'Возникла ошибка при удалении сообщения: {e}')
        pass
    await state.set_state(EditMessage.number)


@admin_router.message(EditMessage.number)
async def upload_new_file(msg: Message, state: FSMContext, bot: Bot):
    data = await state.get_data()
    try:
        msg_to_delete = await msg.answer(f'Прошлый текст сообщения {msg.text}:\n\n'
                                         f'{msgs[msg.text]}\n\n'
                                         f'<b>Введите новый:</b>',
                                         reply_markup=await cancel_state_kb(),
                                         parse_mode='HTML')
        await state.update_data(number=msg.text)
        await state.set_state(EditMessage.text)
    except:
        msg_to_delete = await msg.answer('Номер этого сообщения не обнаружен!\n'
                                         'Сообщение 1 и 2 отправляются в начале\n'
                                         'Сообщение 3 отправляется вместе с файлом\n',
                                         reply_markup=await cancel_state_kb())
    finally:
        await state.update_data(msg_to_delete=msg_to_delete.message_id)
        await bot.delete_message(chat_id=msg.chat.id, message_id=int(data['msg_to_delete']))


@admin_router.message(EditMessage.text)
async def upload_new_file(msg: Message, state: FSMContext, bot: Bot):
    data = await state.get_data()
    await update_message_in_file(msg.text, int(data['number']) - 1)
    await msg.answer(f'Новый текст для сообщения {data['number']} успешно установлен!')
    await bot.delete_message(chat_id=msg.chat.id, message_id=int(data['msg_to_delete']))
    await state.clear()
