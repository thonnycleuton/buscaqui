from django import forms
from selectable.forms import AutoCompleteWidget
from busca.buscalookup import BuscaLookup

from busca.models import Busca


class BuscaForm(forms.ModelForm):

    class Meta:
        model = Busca
        fields = '__all__'

    q = forms.CharField(
        label='Search',
        widget=AutoCompleteWidget(BuscaLookup),
        required=False,)
