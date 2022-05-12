from datetime import date

import vk

from const import ACCESS_TOKEN, MY_USER_ID

# Открытие сессии, авторизация через полученный access-token
session = vk.Session(
    access_token=ACCESS_TOKEN)
vkapi = vk.API(session, v='5.131')

# Получает данные всех друзей авторизованного пользователя + дату ДР
check_friends = vkapi.friends.get(user_id=MY_USER_ID,
                                  fields='bdate')
friends_info = check_friends['items']
now = date.today()
currentdate = '%s.%s' % (now.day, now.month)

# Сравнивает дату ДР друга с сегодняшней датой, если == поздравляет друга
for friend in friends_info:
    if 'bdate' in friend:
        friend_birthday = '.'.join(friend['bdate'].split('.')[0:2])
        if friend_birthday == currentdate:
            message = (f'@id{friend["id"]} ({friend["first_name"]}'
                       f'{friend["last_name"]}) поздравляю с Днём рождения!!!')
            print(message)
            hp_message = vkapi.wall.post(message=message)
# Выводит в терминал количество друзей пользователя
print('Количество друзей: %d' % check_friends['count'])
