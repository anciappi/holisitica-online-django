from django.urls import path

from . import views

urlpatterns = [
    # PAGINA DE INICIO + SECCIONES
    path("", views.HomeView.as_view(), name="home"),
    path("about/", views.AboutView.as_view(), name="about"),
    path("contacto/", views.ContactView.as_view(), name="contacto"),
    path("terapias/", views.TeraphyView.as_view(), name="terapias"),
    path("aranceles/", views.ArancelesView.as_view(), name="aranceles"),
    path("terapeutas/", views.teraphistsView.as_view(), name="terapeutas"),

    # REGISTER
    path("register/", views.RegisterView.as_view(), name="registro"),
]