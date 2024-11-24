<strong>Инструкция по запуску на Windows:</strong>

<b>1. Установите [Python 3.12](https://www.python.org/downloads/release/python-3127/).</b><br>
    Не забудьте поставить галочку Add to Path.</b><br>
    Проверить версию можно в консоли: ```python --version``` или ```python3 --version```

<b>2. Создайте и активируйте виртуальное окружение.</b><br>
    Для начала перейдите в корневую директорию, например: ```cd C:\Users\user\Desctop\TgBot```<br>
    Чтоб создать, напишите в консоль: ```python -m venv venv```<br>
    Чтоб активировать: ```.\venv\Scripts\activate```

<b>3. Установите зависимости.</b><br>
    В консоль: ```pip install -r requirements.txt```

<b>4. Вставьте свои значения в config.py:</b><br>
    Перейдите в [BotFather](https://t.me/BotFather) в Telegram и создайте нового бота, после чего он выдаст вам токен, который нужно вставить в перемунную TOKEN_BOT = "токен".<br>
    Внутрь переменной ADMINS вставьте telegram id админов через запятую

<b>5. Запуск бота:</b><br>
    В консоль: ```python main.py``` или ```python3 main.py```
