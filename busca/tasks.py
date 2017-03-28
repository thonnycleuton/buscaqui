import json
import urllib2
from random import randint
from busca.models import Busca
from celery.task import task


def get_randomic_data():
    """metodo que busca elementos em randomuser"""
    url = 'http://api.randomuser.me/'
    open_url = urllib2.urlopen(url).read()
    objects = json.loads(open_url)
    return objects['results'][0]


def add_object(numero):
    """metodo que busca emails dentro da lista de objetos buscados e salva no banco"""
    data_api_objs = get_randomic_data()

    busca_obj = Busca()
    busca_obj.email = '%s' % (data_api_objs['email'])
    busca_obj.number = numero
    busca_obj.save()


@task(name="add_objects")
def add_objects(quant):
    for i in range(quant):
        numero = randint(0, quant)
        add_object(numero)
