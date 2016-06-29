from busca.models import Busca

from busca.form import BuscaForm
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.views.generic import ListView, CreateView, DeleteView, UpdateView


class BuscaCreate(CreateView):
    model = Busca
    template_name = 'form.html'

    def form_valid(self, form):
        form.save()
        messages.success(self.request, ('Salvo com sucesso!'))
        return redirect('home')


class BuscaView(ListView):
    template_name = 'list.html'
    model = Busca
    paginate_by = 100

    def get(self, request, **kwargs):
        self.object_list = self.get_queryset()
        if 'q' in request.GET:
            self.object_list = self.object_list.filter(text__icontains=request.GET.get('q'))

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
        messages.error(self.request, ('Deletado com sucesso!'))
        return HttpResponseRedirect(success_url)


class BuscaUpdate(UpdateView):
    model = Busca
    template_name = 'form.html'

    def form_valid(self, form):
        form.save()
        messages.success(self.request, ('Alterado com sucesso!'))
        return redirect('home')