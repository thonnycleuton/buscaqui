from selectable.base import ModelLookup
from selectable.registry import registry
from busca.models import Busca


class BuscaLookup(ModelLookup):
    model = Busca
    search_fields = ('email__icontains', )


registry.register(BuscaLookup)
