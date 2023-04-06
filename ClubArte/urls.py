from django.urls import path
from ClubArte.views import *

urlpatterns = [
    path("", Main, name="ClubArteMain"),
    path("Poesia/Crear/",poesia_crear, name="CrearPoesia"),
    path("Poesia/Eliminar/<int:id_poesia>", poesia_elim, name="EliminarPoesia"),
    path("Poesia/Modificar/<int:id_poesia>", poesia_modif, name="ModificarPoesia"),
    path('Poesia/Ver/<int:id_poesia>', poesia_ver, name='PoesiaVer'),
    path('Poesia/Buscar/', poesia_buscar, name='PoesiaBuscar'),
    path('Poesia/BuscarVer/', poesia_buscar_ver, name='PoesiaBuscarVer'),

]