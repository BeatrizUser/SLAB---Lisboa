from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = "Cadastro"
urlpatterns = [
    path("", views.CadListView.as_view(), name="list"),
    path("<slug:slug>/", views.CadDetailView.as_view(), name="detail"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)