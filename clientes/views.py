from dataclasses import fields

from django.shortcuts import render
from .models import Cliente,Carro
from django.http import HttpResponse, JsonResponse
import re
from django.core import serializers
import json
from django.views.decorators.csrf import csrf_exempt

def clientes (request):
    if request.method == "GET":
        clientes_list = Cliente.objects.all()
        return render(request, 'clientes.html' ,{'clientes':clientes_list})
    elif request.method == "POST":
        nome = request.POST.get('nome')
        sobrenome = request.POST.get('sobrenome')
        email = request.POST.get('email')
        cpf = request.POST.get('cpf')

        carros = request.POST.getlist('carro')
        placas = request.POST.getlist('placa')
        anos = request.POST.getlist('ano')

        cliente = Cliente.objects.filter(cpf = cpf)
        if cliente.exists():

            return render(request, 'clientes.html', {'nome':nome, 'sobrenome':sobrenome, 'email':email, 'carros':zip(carros,placas,anos)})
        if not re.fullmatch(re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+'), email):

            return render(request, 'clientes.html', {'nome':nome, 'sobrenome':sobrenome,'cpf':cpf, 'zip': zip(carros,placas,anos)})

        cliente = Cliente(
            nome = nome,
            sobrenome = sobrenome,
            email = email,
            cpf = cpf,
        )

        cliente.save()

        for carro, placa, ano in zip(carros, placas, anos):
            car = Carro(
                carro = carro,
                placa = placa,
                ano = ano,
                cliente = cliente,
            )
            car.save()

        return HttpResponse('teste')


def att_cliente(request):
    id_cliente = request.POST.get('id_cliente')
    cliente = Cliente.objects.filter(id=id_cliente)
    carros = Carro.objects.filter(cliente=id_cliente[0])

    cliente_json = json.loads(serializers.serialize('json', cliente))[0]['fields']
    carros_json = json.loads(serializers.serialize('json', carros))
    carros_json = [{'fields': carro['fields'], 'id': carro['pk']}for carro in carros_json]

    data = {'cliente' : cliente_json, 'carros': carros_json}

    return JsonResponse(data)


@csrf_exempt
def update_carro(request,id):
    nome_carro = request.POST.get('carro')
    placa = request.POST.get('placa')
    ano = request.POST.get('ano')

    carro = Carro.objects.get(id=id)
    list_carros = Carro.objects.filter(placa=placa).exclude(id=id)

    if list_carros.exists():
        return HttpResponse("Placa já existente")

    carro.carro = nome_carro
    carro.placa = placa
    carro.ano = ano
    carro.save()

    return HttpResponse(nome_carro)