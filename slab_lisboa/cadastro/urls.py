from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from cadastro.views import CadastroList

app_name = "Cadastro"
urlpatterns = [
    path("", views.CadListView.as_view(), name="list"),
    path('busca/', CadastroList.as_view({'get': 'list'}), name="Busca"),
    path("detalhes/<slug:slug>/", views.CadDetailView.as_view(), name="detail"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)