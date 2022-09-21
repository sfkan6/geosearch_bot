from aiogram import types

from bot.api_module import *
from bot.locale import *
from bot.settings import clientDB


async def _select_obj(message, state, response, view, mode):
    if response:
        if len(response) == 1:
            obj = response[0]
            geo_data = obj['geometry']['coordinates']
            await message.answer(view(obj))
            await message.answer_location(geo_data[1], geo_data[0])
        else:
            keyboard = keyboard_resp(response, mode)
            await state.update_data(response=response)
            await message.answer(select_add, reply_markup=keyboard)
    else:
        await message.answer(nothing_found)


async def search_org(message, state):
    '''Search for organizations'''
    data = await state.get_data()
    data = data.get('response')
    response = None

    if data:
        for org in data:
            org_name = collect_header(org, 'CompanyMetaData', 'name', 'address')
            if org_name.startswith(message.text[:-3]):
                response = [org]
                break

    if not response:
        response = await get_api_search_org(
            await clientDB.get_key(message.from_user.id), message.text, type='biz'
        )
    await _select_obj(message, state, response, reply_org, 'org')


async def search_geo_name(message, state):
    '''Search for GeoObjs'''
    data = await state.get_data()
    data = data.get('response')
    response = None

    if data:
        for geo in data:
            geo_name = collect_header(geo)
            if geo_name.startswith(message.text[:-3]):
                response = [geo]
                break

    if not response:
        response = await get_api_search_org(
            await clientDB.get_key(message.from_user.id), message.text, type='geo'
        )
    await _select_obj(message, state, response, reply_geo, 'geo')


async def get_near(message, state):
    '''Search for nearby objects'''
    data = await state.get_data()
    data = data.get('response')
    response = None

    if data:
        for org in data:
            org_name = collect_header(org, 'CompanyMetaData', 'name', 'address')
            if org_name.startswith(message.text[:-3]):
                response = [org]
                break
    if not response:
        data = await state.get_data()
        data = data.get('geo')
        spn = [0.2, 0.2]
        kwargs = {'ll': data, 'spn': spn, 'type': 'biz'}
        response = await get_api_search_org(
            await clientDB.get_key(message.from_user.id), message.text, **kwargs
        )
    await _select_obj(message, state, response, reply_org, 'org')


async def get_image(message, bot):
    '''Image search by geodata'''
    data = message.text.split(',')
    query = list(reversed(data[0].split()))
    params = {}
    if len(data) >= 2:
        params['z'] = data[1]
    try:
        response = await get_api_image(query, **params)
        await bot.send_photo(
            message.chat.id, types.BufferedInputFile(response, filename='yandex_map.png')
        )
    except:
        await message.answer(error_img)


async def update_search_org_key(message, bot):
    '''Control Panel Keys'''
    if await clientDB.change_key(message.from_user.id, message.text):
        await message.answer(reply_key_update(message.text))
    else:
        await message.answer(error_bd)
    await bot.delete_message(message.chat.id, message.message_id)
