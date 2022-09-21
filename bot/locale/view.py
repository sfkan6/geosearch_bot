from os import name
from aiogram import types
from .ru import *


# get mode or help
def reply_start(username):
    return text_start.format(username=username)


def reply_key_update(key):
    key = '*' * len(key) + key[-4:]
    return key_updeted.format(key=key)


def get_primary_keys():
    return PRIMARY_KEYS


def get_primary_help():
    return '\n'.join(PRIMARY_HELP)


def get_secondary_keys(num=0):
    return get_secondary_all()[num]


def get_secondary_all(in_one=False):
    if in_one:
        return ONE_SECOND_KEYS + TWO_SECOND_KEYS
    return [ONE_SECOND_KEYS, TWO_SECOND_KEYS]


def get_secondary_help(key):
    return VIEW_TREE_HELP.get(key)


def get_secondary_help_all():
    return ONE_SECOND_HELP + TWO_SECOND_HELP


# collect response with latitude and longitude
def reply_org(org):
    text = []
    if org_meta := org['properties'].get('CompanyMetaData'):
        text.append(f'<b>{name}</b>: {org_meta["name"]}')
        if description := org_meta.get('description'):
            text.append(description)
        if add := org_meta.get('address'):
            text.append(f'<b>{address}</b>: <code>{add}</code>')
        if urls := org_meta.get('url'):
            text.append(f'<b>{url}</b>: {urls}')
        if categories := org_meta.get('Categories'):
            text.append(f'<b>{categories_text}</b>:')
            for categ in categories:
                text.append('\t\t' + categ['name'])
        if phones := org_meta.get('Phones'):
            text.append(f'<b>{phones_text}</b>:')
            for phone in phones:
                phone = f'{phone.get("type", "")}: <code>{phone.get("formatted")}</code>'
                text.append('\t' + phone)
        if hours := org_meta.get('Hours'):
            text.append(f'<b>{work_hours}</b>: {hours.get("text")}')

    geo_coord = org['geometry']['coordinates']
    text.append(
        f'<b>{lat_text} {long_text}</b>:\n<code>{geo_coord[1]} {geo_coord[0]}</code>'
    )
    return '\n'.join(text)


def reply_geo(geo):
    text = []
    if geo_meta := geo['properties'].get('GeocoderMetaData'):
        if description := geo_meta.get('description'):
            text.append(description)
        if kind := geo_meta.get('kind'):
            text.append(f'<b>{kind_text}</b>: {kind_code.get(kind, kind)}')
        if add := geo_meta.get('text'):
            text.append(f'<b>{address}</b>: <code>{add}</code>')

    geo_coord = geo['geometry']['coordinates']
    text.append(
        f'<b>{lat_text} {long_text}</b>:\n<code>{geo_coord[1]} {geo_coord[0]}</code>'
    )
    return '\n'.join(text)


# Keyboard
def geosearch_kb():
    keys = ONE_SECOND_KEYS
    keys = [
        [
            types.KeyboardButton(text=keys[0]),
            types.KeyboardButton(text=keys[1])
        ], [
            types.KeyboardButton(text=keys[2], request_location=True),
            types.KeyboardButton(text=keys[3])
        ], [
            types.KeyboardButton(text=text_exit)
        ]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=keys, resize_keyboard=True)
    return keyboard


def settings_kb():
    keys = TWO_SECOND_KEYS
    keys = [[types.KeyboardButton(text=keys[0]), types.KeyboardButton(text=text_exit)]]
    keyboard = types.ReplyKeyboardMarkup(keyboard=keys, resize_keyboard=True)
    return keyboard


def primary_kb():
    keys = get_primary_keys()
    keys = [
        [types.KeyboardButton(text=keys[0]), types.KeyboardButton(text=keys[1])],
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=keys, resize_keyboard=True)
    return keyboard


def collect_header(elem, meta='GeocoderMetaData', name='kind', address='text'):
    header = []
    if name := elem['properties'].get(meta, {}).get(name):
        header.append(kind_code.get(name, name))
    if address := elem['properties'].get(meta, {}).get(address):
        header.append(address)
    return ', '.join(header)


def keyboard_resp(elems, org='org'):
    keys = []
    keys.append([types.KeyboardButton(text=text_back)])
    for elem in elems:
        if org == 'org':
            keys.append(
                [types.KeyboardButton(
                    text=collect_header(elem, 'CompanyMetaData', 'name', 'address')
                )]
            )
        else:
            keys.append([types.KeyboardButton(text=collect_header(elem))])
    return types.ReplyKeyboardMarkup(keyboard=keys, resize_keyboard=True)
