# Интернет-магазин на Django

Учебный проект интернет-магазина, разрабатываемый в рамках курса. На текущем этапе реализованы главная страница и страница контактов с формой обратной связи.

## Технологии

- Python 3.10+
- Django 4.2+
- Bootstrap 5 (CDN)

## Структура проекта

```
web_contacts/
├── catalog/                # Основное приложение
│   ├── templates/
│   │   └── catalog/
│   │       ├── home.html   # Главная страница
│   │       └── contacts.html # Страница контактов с формой
│   ├── urls.py             # Маршруты приложения
│   └── views.py            # Контроллеры
├── config/                 # Настройки проекта Django
│   ├── settings.py
│   └── urls.py             # Корневые маршруты (include)
├── old_version/            # Архив старой версии (чистый Python)
│   ├── server.py
│   └── templates/          # Старые HTML-прототипы
├── manage.py
├── requirements.txt        # Зависимости
└── README.md
```
## Начало работы

### Создайте и активируйте виртуальное окружение

```
python -m venv venv
# Windows:
venv\Scripts\activate
# Linux/macOS:
source venv/bin/activate
```
### Установите зависимости

```
pip install -r requirements.txt
```

### Выполните миграции (создание базы данных)

```
python manage.py migrate
```

### Запустите сервер разработки

```
python manage.py runserver
```

## Откройте в браузере

```
Главная страница: http://127.0.0.1:8000/
Контакты: http://127.0.0.1:8000/contacts/
```






