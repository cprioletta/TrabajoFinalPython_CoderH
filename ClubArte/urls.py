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

    path("Cine/Crear/", cine_crear, name="CrearCine"),
    path("Cine/Eliminar/<int:id_movie>", cine_elim, name="EliminarCine"),
    path("Cine/Modificar/<int:id_movie>", cine_modif, name="ModificarCine"),
    path('Cine/Ver/<int:id_movie>', cine_ver, name='VerCine'),
    path('Cine/Buscar/', cine_buscar, name='BuscarCine'),
    path('Cine/BuscarVer/', cine_buscar_ver, name='BuscarVerCine'),

    path('Foto/Crear/', foto_crear, name='CrearFoto'),
    path('Foto/Buscar/', foto_buscar, name='BuscarFoto'),
    path('Foto/Eliminar/<int:id_foto>', foto_eliminar, name='EliminarFoto'),
    path('Foto/Modificar/<int:id_foto>', foto_modificar, name='ModifFoto'),
    path('Foto/BuscarVer/', foto_buscar_ver, name='BuscarVerFoto'),
    path('Foto/Ver/<int:id_foto>', foto_ver, name='VerFoto'),

]