from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Members
from django.urls import reverse

# Create your views here.

def index(request):
    meusMembros = Members.objects.all().values()
    template = loader.get_template('index.html')
    context = {
        'meusMembros': meusMembros,
    }
    return HttpResponse(template.render(context, request))

def add(request):
    template = loader.get_template("add.html")
    return HttpResponse(template.render({}, request))

def addrecord(request):
    x = request.POST['nome']
    y = request.POST['sobrenome']
    member = Members(nome=x, sobrenome=y)
    member.save()
    return HttpResponseRedirect(reverse('index'))

def delete(request, id):
    member = Members.objects.get(id=id)
    member.delete()
    return HttpResponseRedirect(reverse('index'))

def update(request, id):
    membro = Members.objects.get(id=id)
    template = loader.get_template("update.html")
    context = {
        'membro': membro,
    }
    return HttpResponse(template.render(context, request))

def updaterecord(request, id):
    nome = request.POST['nome']
    sobrenome = request.POST['sobrenome']
    membro = Members.objects.get(id=id)
    membro.nome = nome
    membro.sobrenome = sobrenome
    membro.save()
    return HttpResponseRedirect(reverse('index'))

def template(request):
    membros = Members.objects.all().values()
    template = loader.get_template('template.html')
    context = {
        'membros':membros,
    }
    return HttpResponse(template.render(context, request))

