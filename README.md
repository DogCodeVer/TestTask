# TestTask Digital Dialog README

## Установка и настройка

### Предварительные требования
- Python 3.8+
- pip
- virtualenv (рекомендуется)
- PostgreSQL или другая поддерживаемая база данных

### Шаги установки

1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/username/repository.git
   cd repository
   ```

2. Создайте виртуальное окружение и активируйте его:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Установите зависимости:
   ```bash
   pip install -r requirements.txt
   ```

4. Выполните миграции базы данных:
   ```bash
   python manage.py migrate
   ```

5. Запустите сервер разработки:
   ```bash
   python manage.py runserver
   ```
6. Создайте пользователя:
   ```bash
   python manage.py createsuperuser
   ```
8. Откройте проект в браузере по адресу [http://localhost:8000/admin](http://localhost:8000/admin).

## Контакты
Если у вас есть вопросы или предложения, пожалуйста, свяжитесь с нами:
- Email: sheremetvadim09@gmail.com
- Telegram: [@dogver](https://t.me/dogver)

## Благодарности
Особая благодарность команде Django и DaData за их отличные инструменты и сервисы.

