# Получение фото от NASA и публикация их на канал в телеграме

### Как установить

Python3 должен быть уже установлен.
Затем используйте `pip` (или `pip3`, есть конфликт с Python2) для установки зависимостей:

```
pip install -r ./requirements.txt
```

### Примеры запуска

Для получения фото APOD:
```
python get_photo_apod.py
```
Для получения фото EPIC:
```
python get_epic_images.py
```
Для получения фото Last launch:
```
python fetch_spacex_last_launch.py
```
Чтобы начать выкладывать фото в телеграм канал:
```
python telegram_bot.py
```

### Переменные окружения

Чтобы получить ключь от NASA перейдите по ссылке https://api.nasa.gov/#signUp,
чтобы получить ключь от телеграма вам нужно создать бота в https://t.me/BotFather, также нужно будет создать телеграм канал и добавть туду бота как администратора
Также нужно в папке проекта создать файл .env и засунуть туда ключи:
```
NASA_KEY = "здесь должен быть ключь от nasa"
TELEGRAM_KEY = "здесь должен быть ключь от телегрма"
CHAT_ID = "здесь должен быть адрес на канал"
```

### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).
