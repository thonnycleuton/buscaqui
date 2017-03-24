=============================
django-telegrambot
=============================

.. image:: https://badge.fury.io/py/django-telegrambot.png
    :target: https://badge.fury.io/py/django-telegrambot

.. image:: https://travis-ci.org/JungDev/django-telegrambot.png?branch=master
    :target: https://travis-ci.org/JungDev/django-telegrambot

A simple app to develop Telegram bots with Django

# Buscaqui

Buscaqui é um projeto simples em python/Django que faz a geração assíncrona de dados a partir da api randu para popular este sistema .
O que ele faz? Este projeto simplesmente exibe uma lista paginável de enderecos de email gerados via requisição externa a API http://api.randuser.me e tambem gerando numeros randomicamente com a biblioteca random. Alem disso, possui um campo de busca com autocomplete para melhor busca dos endereços buscados.

Para gerar uma base de dados consumindo recursos da api Randuser é necessário rodar o comando abaixo: python manage.py buscar ele trará 300 enderecos de email que povoarão uma tabela do BD. O Sistema esta rodando em: http://q-buscador.herokuapp.com/ acesse.

## Rodando localmente

Make sure you have Python [installed properly](http://install.python-guide.org).  Also, install the [Heroku Toolbelt](https://toolbelt.heroku.com/) and [Postgres](https://devcenter.heroku.com/articles/heroku-postgresql#local-setup).

```sh
$ git clone git@github.com:thonnycleuton/buscaqui.git
$ cd buscaqui

$ pip install -r requirements.txt

$ createdb buscaqui

$ python manage.py migrate
$ python manage.py collectstatic

```

Voce entao podera roda-lo localmente em [localhost:8000](http://localhost:8000/).
