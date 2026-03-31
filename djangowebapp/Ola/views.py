#criando o que será exibido para  usuario
from django.http import HttpResponse
from django.shortcuts import render


#cria sua views aqui
def index(request):
    return render(request, "Ola/desafio10site.html")


def joab(request):
    return HttpResponse("Olá, Joab!")


def saudacao(request, name):
    #capitalize faz a 1° letra da palavra ficar maiuscula
    return HttpResponse(f"Olá, {name.capitalize()}!")
def saudacao_render(request,name):
    return render(request, "saudacao/saudacao.html", {"name":name.capitalize()})
