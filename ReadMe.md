Для запуска веб-сервиса и его теста сначало надо установить
библиотеку virtualenv и создать виртуальное окружение.

1. установить pip - **sudo apt-get install python3-pip**
2. установить virtualenv - **sudo pip3 install virtualenv**
3. создать виртуальное окружение - **mkvirtualenv %имя_окружения**
4. Если это не сработало, то использовать -
**apt-get install python3-venv**
5. Создать виртуольное окружение - **python3 -m venv %имя_окружения**
6. Запуск окружение - **source %имя_окружения/bin/activate**
7. Создать локальный репозиторий - **git init**
8. Склонировать удаленный репозиторий -
**git clone https://github.com/NILegio/gcore-labs-test**
9. Установить необходимые библиотеки -
**pip install -r requirenents.txt**

Запуск веб-сервиса - **python3 prime_number.py**

Запуск теста - **pytest**