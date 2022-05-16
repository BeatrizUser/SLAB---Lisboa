from django.views.generic import DetailView, ListView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from cadastro.api.serializers import CadastroSerializer
from rest_framework import viewsets, permissions
from .models import Cadastro

class CadListView(ListView):
    model = Cadastro

class CadDetailView(DetailView):
    model = Cadastro

class CadastroList(viewsets.ModelViewSet):
  queryset = Cadastro.objects.all()
  serializer_class = CadastroSerializer
  permission_classes = [permissions.IsAuthenticated]
  filter_backends = [DjangoFilterBackend, SearchFilter]
  filterset_fields = ['nome_completo_aluno']
  search_fields = ['nome_completo_aluno', 'slug',]