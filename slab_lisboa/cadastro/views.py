from django.views.generic import DetailView, ListView
from .models import Cadastro

class CadListView(ListView):
    model = Cadastro

class CadDetailView(DetailView):
    model = Cadastro