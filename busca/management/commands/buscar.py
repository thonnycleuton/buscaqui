import json
import urllib2
from random import randint

from busca.models import Busca
from django.core.management import BaseCommand


def get_randomic_data():
    url = 'http://api.randomuser.me/'
    open_url = urllib2.urlopen(url).read()
    objects = json.loads(open_url)
    return objects['results'][0]


def add_object():
    data_api_objs = get_randomic_data()

    busca_obj = Busca()
    busca_obj.text = '%s' % (data_api_objs['email'])
    busca_obj.number = randint(0, 300)
    busca_obj.save()


def add_objects():
    for i in range(300):
        add_object()


class Command(BaseCommand):

    help = "testando essa porra"

    def handle(self, *args, **options):
        add_objects()
        self.stdout.write("Doing all the things!")

