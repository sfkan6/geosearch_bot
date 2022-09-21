
# Приветствие
text_start = 'Привет {username}'

# text for select_primary_key()
select_mode = 'Выберите режим:'

# text for select_primary_key()
select_method = 'Выберите метод:'

# latitude and longitude
lat_text = 'Широта'
long_text = 'Долгота'

# instructions
select_add = 'Выберите адрес:'
try_later = 'Попробуйте позже'
nothing_found = 'Ничего не найдено'

geopos_updated = 'Геокоординаты обновлены'

# back text
text_back = 'Назад'

# exit text
text_exit = 'Выход'

# reply response
name = 'Название'
address = 'Адрес'
url = 'URL'
phones_text = 'Номера'
categories_text = 'Категории организации'
work_hours = 'Время работы'


kind_text = 'Местность'
kind_code = {
    "house": "Дом",
    "street": "Улица",
    "metro": "Станция метро",
    "district": "Район города",
    "locality": "Населенный пункт",
    "area": "район области",
    "province": "область",
    "country": "страна",
    "region": "Регион",
    "hydro": "река / озеро / ручей / водохранилище и т. п.",
    "railway_station": "ж.д. станция",
    "station": "станции, не относящиеся к железной дороге",
    "route": "линия метро / шоссе / ж.д. линия",
    "vegetation": "лес / парк / сад",
    "airport": "аэропорт",
    "entrance": "подъезд / вход",
    "other": "прочее",
}

error_img = 'Неверный запрос'

error_key = 'Неверный токен Yandex maps'

error_query = 'Неверный токен или ключ'

key_updeted = 'Ключ успешно изменён:\n{key}'

error_bd = 'Возникла ошибка, повторите запрос'

# Keyboard
# Первичное меню
PRIMARY_KEYS = ['Геопоиск', 'Настройки']

# Вторинчное меню
ONE_SECOND_KEYS = [
    'Организации',
    'Топонимы',
    'Ближайшее место',
    'Получить изображение',
]

TWO_SECOND_KEYS = [
    'Key №1'
]

# Help
# Helper's первичного меню
PRIMARY_HELP = ['''
Геопоиск включает в себя 4 метода:
<b>Организации</b> - Поиск по организациям
<b>Топонимы</b> - поиск по топонимам и адресам
<b>Ближайшее место</b> - поиск ближайшего похожего места
<b>Получить изображение</b> - возвращает изображение

Чтобы получить более подробную информацию
зайдите в режим и отправьте 'help'
''', '''
Функции поиска используют API Яндекс Карт,
добавьте свой ключ 'API Поиска по организациям'
в настройках.
Для получение изображения ключ не нужен

Получить ключ:
https://developer.tech.yandex.ru/services/
''']

# Helper's вторичного меню
ONE_SECOND_HELP = ['''
Выполняет поиск по Организациям
''', '''
Выполняет поиск по Топонимам
''', '''
Выполняет поиск ближайшего места по запросу
''', '''
Возвращает изображение
Введите запрос вида:
[Широта] [Долгота],[Z]
Z - (0-17) уровень приближения

Примеры:
55.753933 37.620735
55.753933 37.620735,16
''']

TWO_SECOND_HELP = ['''
Добавить или изменить API ключ
для поиска по организациям и топонимам
''']


# dictionary mode - description
VIEW_TREE_HELP = {
    x: y for x, y in
    zip(ONE_SECOND_KEYS + TWO_SECOND_KEYS, ONE_SECOND_HELP + TWO_SECOND_HELP)
}
