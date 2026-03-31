#criando ulrs pesmitidas para este app

from django.urls import path
from . import views

urlpatterns = [
    path("",views.index, name="index"),
    #com str:name definido o caminho para qualquer que seja a entrada na url
    path("<str:name>", views.saudacao_render, name="saudacao")
]