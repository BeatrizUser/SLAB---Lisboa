from django.urls import path
from . import views

app_name = "Cadastro"
urlpatterns = [
    path("", views.CadListView.as_view(), name="list"),
    path("<slug:slug>/", views.CadDetailView.as_view(), name="detail")
]