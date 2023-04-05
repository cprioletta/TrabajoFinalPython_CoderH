from django.urls import path
from ClubArte.views import *

urlpatterns = [
    path("", Main, name="ClubArteMain"),

]