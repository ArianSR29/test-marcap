from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import ListView, CreateView

from apps.cellphonesControl.models import RecepcionMercancia, OrdenCompra
from apps.cellphonesControl.forms import RecepcionForm, OrdenCompraForm

# Create your views here.

def index_recepcion(request):
    return HttpResponse("Soy la página principal de las recepciones")
    
class RecepcionListView(ListView):
    model = Recepcion
    template_name = "recepcion/recepcion_list.html"


class RecepcionCreateView(CreateView):
    model = Recepcion
    template_name = "recepcion/recepcion_form.html"
    form_class = RecepcionForm
    second_form_class = OrdenCompraForm
    success_url = reverse_lazy('recepcion:recepcion_listar')

    def def get_context_data(self, **kwargs):
        context = super(RecepcionCreateView, self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)
        if 'form2' not in contex:
            context['form2'] = self.second_form_class(self.request.GET)
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        form = self.form_class(request.POST)
        form2 = self.second_form_class(request.POST)

        if form.is_valid() and form2.is_valid():
            solicitud = form.save(commit=False)
            solicitud.OrdenCompra = form2.save()
            solicitud.save()
            return HttpResponseRedirect(self.get_success_url())