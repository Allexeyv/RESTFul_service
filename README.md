# RESTFul_service

## Task description
1. RESTFul сервис на базе django (sqlite база пользователей)
- JWT авторизация (через jwt token, сроком на сутки, если данные не верны или истек токен - 401 Unauthorized) (добавить пару аккаунтов)
- resources (с проверкой авторизации)
- publications (публикации, генерятся через faker: title, text, created_at, tags)
- categories (категории, генерятся через faker: name, created_at)

2. api client библиотека
- принцип работы:
``` sh
    from api_lib import ApiClient
    base_url = http://api_address/
    client = ApiClient(base_url=base_url)
    login_result = client.login(ligin, pass)
    # сохраняется атрибут token, доступный затем как client.token

    publications = client.get_publications()
    categories = client.get_categories()

    publication = client.get_publication(id=1)
    category = client.get_category(id=1)

    client.update_category(data=category)
    client.update_publication(data=publication)

    client.create_category(data=category)
    client.create_publication(data=publication)
```

## How to start
``` sh
git clone git@github.com:Allexeyv/RESTFul_service.git
pip install virtualenv
python -m venv venv
source venv/bin/activate
cd RESTFul_service
pip install --upgrade pip
pip install -r requirements.txt
python manage.py runserver 0.0.0.0:8000
```

## Django admin panel data
login: admin
password: 1111