from busca.models import Busca

from busca.form import BuscaForm
from busca.tasks import add_objects
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.views.generic import ListView, CreateView, DeleteView, UpdateView


class BuscaCreate(CreateView):
    model = Busca
    template_name = 'form.html'
    fields = '__all__'

    def form_valid(self, form):
        form.save()
        messages.success(self.request, 'Salvo com sucesso!')
        return redirect('index')


class BuscaView(ListView):
    template_name = 'index.html'
    model = Busca
    paginate_by = 100

    def get(self, request, **kwargs):
        self.object_list = self.get_queryset()

        if request.GET.get('mybtn'):
            # chama metodo assincrono e passa como parametro a quantidade de registro a serem inseridos
            add_objects(100)

        if 'q' in request.GET:
            # filtra a url capturada pelo metodo GET
            self.object_list = self.object_list.filter(email__icontains=request.GET.get('q'))

        context = super(BuscaView, self).get_context_data(**kwargs)
        context['search'] = BuscaForm()

        return self.render_to_response(context)


class BuscaDelete(DeleteView):
    model = Busca
    success_url = '/'
    template_name = 'delete.html'

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_url = self.get_success_url()
        self.object.delete()
        messages.error(self.request, 'Deletado com sucesso!')
        return HttpResponseRedirect(success_url)


class BuscaUpdate(UpdateView):
    model = Busca
    template_name = 'form.html'
    fields = '__all__'

    def form_valid(self, form):
        form.save()
        messages.success(self.request, 'Alterado com sucesso!')
        return redirect('index')