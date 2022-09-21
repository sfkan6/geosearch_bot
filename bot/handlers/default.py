from aiogram import types, Router, filters
from aiogram.fsm.context import FSMContext
from bot.locale import *


router = Router()


@router.message(commands=['start'])
async def cmd_start(message: types.Message):
    '''Send welcome when the command /start'''
    await message.reply(reply_start(message.chat.username))
    await cmd_help(message)
    await cmd_menu(message)


@router.message(commands=['help'])
async def cmd_help(message: types.Message):
    '''Send instruction when the command /helo'''
    await message.answer(get_primary_help())


@router.message(filters.Text(text=['/menu', text_exit]))
async def cmd_menu(message: types.Message, state: FSMContext = None):
    '''Send reply_markup with primary buttons'''
    if state and await state.get_state():
        await state.clear()
    await message.answer(select_mode, reply_markup=primary_kb())
