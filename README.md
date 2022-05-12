# Happy birthday
С помощью данного скрипта можно поздравить всех друзей именинников с Днём рождения.

### Как запустить
- git clone https://github.com/AlexKrup7/Happy_Birthday_VK_API.git
- pip install requirements.txt
- Авторизоваться на сайте https://vk.com/
- Создать Standalone-приложение https://vk.com/editapp?act=create
- Получить access-token по инструкции https://dev.vk.com/api/access-token/implicit-flow-user
- В файле const.py заполнить MY_USER_ID(id авторизированного пользователя) ACCESS_TOKEN(полученный access-token)
- python happy_birthday.py

