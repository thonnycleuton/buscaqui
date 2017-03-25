from busca.views import BuscaView, BuscaCreate, BuscaUpdate, BuscaDelete
from django.conf.urls import patterns, url, include

urlpatterns = patterns('',
                       (r'^selectable/', include('selectable.urls')),
                       (r'^buscar/', include('haystack.urls')),
                       url(r'^$', BuscaView.as_view(), name='index'),
                       url(r'^criar/$', BuscaCreate.as_view(), name='create'),
                       url(r'^editar/(?P<pk>\d+)/$', BuscaUpdate.as_view(), name='edit'),
                       url(r'^excluir/(?P<pk>\d+)/$', BuscaDelete.as_view(), name='delete'),
                       )
