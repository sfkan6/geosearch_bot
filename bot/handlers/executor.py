from aiogram import types, Router
from aiogram.filters import Text
from aiogram.fsm.context import FSMContext

from bot.models import InputForm
from bot.services import *
from bot.locale import *


router = Router()


@router.message(Text(text=[text_back]))
async def cmd_back(message: types.Message):
    '''Displays modes'''
    await message.answer(
        select_method, reply_markup=geosearch_kb()
    )


@router.message(Text(text=get_primary_keys()))
async def give_secondary_keys(message: types.Message):
    '''Send secondary keys'''
    text = message.text
    keys = get_primary_keys()

    if text == keys[0]:
        keyboard = geosearch_kb() 
    else:
        keyboard = settings_kb()
    await message.answer(select_method, reply_markup=keyboard)


@router.message(Text(text=get_secondary_all(True)))
async def enable_method(message: types.Message, state: FSMContext):
    '''Turns on the selected mode'''
    await state.set_state(InputForm.method)
    await state.update_data(method=message.text)
    await state.set_state(InputForm.query)
    await message.answer(get_secondary_help(message.text))


@router.message(content_types="text", state=InputForm.query)
async def executeer(message: types.Message, state: FSMContext, bot):
    '''Executer a command or request'''
    method = await state.get_data()
    method = method['method']

    if message.text in get_secondary_all():
        await state.clear()
        return await enable_method(message, state)
    elif message.text == 'help':
        return await message.answer(get_secondary_help(method))

    keys = get_secondary_all(True)
    if method == keys[0]:
        await search_org(message, state)
    elif method == keys[1]:
        await search_geo_name(message, state)
    elif method == keys[2]:
        await get_near(message, state)
    elif method == keys[3]:
        await get_image(message, bot)
    elif method == keys[4]:
        await update_search_org_key(message, bot)


@router.message(content_types='location', state='*')
async def get_user_location(message: types.Message, state: FSMContext):
    '''Get user location and enable mode'''
    # enable mode get_near
    await state.set_state(InputForm.method)
    await state.update_data(method=get_secondary_keys()[2])
    # get location data
    await state.update_data(
        geo=[message.location.longitude, message.location.latitude]
    )
    # start mode get_near
    await state.set_state(InputForm.query)
    await message.answer(geopos_updated)
