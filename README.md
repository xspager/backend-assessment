# Solução para Backend Assessment

Utilizando [Django](https://www.djangoproject.com) e [Django REST Framework](https://www.django-rest-framework.org/)

Utilize um virtualenv para rodar o código localmente:

```bash
$ python3 -m venv .env
$ source .env/bin/activate
(.env) $ pip install -r requirements.txt
```

Os testes podem ser rodados com:

```bash
(.env) $ ./manage.py test
```

Um servidor de teste pode ser rodado na porta 8000 com:

```bash
(.env) $ ./manage.py runserver 0.0.0.0:8000
```

É possível subir um abiente completo local com Docker usando docker-composer servido na porta 8080:

```bash
$ docker-compose up -d --build
```

Uma vez com um ambiente minimamente proximo de um ambiente de produção é possível realizar um teste de cara com [locust](https://locust.io)

```bash
(.env) $ pip install locust
(.env) $ locust -f jwt_token.py
```
