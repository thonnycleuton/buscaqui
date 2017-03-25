# Buscaqui

Buscaqui é um projeto simples em python/Django que lista, insere, atualiza e deleta emails em uma base de dados (CRUD)*[]: 
Tambem conta com uma ferramenta de busca com autocomplete.


## Uso

O sistema é capaz de gerar, assincronamente, um bloco de 100 endereços de email, no botao superior direirto "+100".
Esses enderecos de email são gerados via requisição externa a API http://api.randuser.me e tambem gerando numeros randomicamente com a biblioteca random. 
Alem disso, possui um campo de busca com autocomplete para melhor busca dos endereços buscados.

O Sistema esta rodando em: http://buscaqui.herokuapp.com/ acesse.

### Instalação

```sh

$ git clone git@github.com:thonnycleuton/buscaqui.git
$ cd buscaqui

$ pip install -r requirements.txt

$ python manage.py migrate
$ python manage.py collectstatic

```
Voce entao podera roda-lo localmente em [localhost:8000](http://localhost:8000/).
