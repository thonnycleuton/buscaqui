from django.db import models


class Busca(models.Model):

    number = models.IntegerField()
    email = models.TextField()

    def __unicode__(self):
        return self.text
