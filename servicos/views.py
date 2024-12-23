from django.shortcuts import render, get_object_or_404
from .forms import FormServico
from django.http import HttpResponse
from .models import Servicos

def novo_servico(request):
    if request.method == "GET":
        form = FormServico()
        return render(request, 'novo_servico.html', {'form': form})
    elif request.method == "POST":
        form = FormServico(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponse('Salvo com sucesso')
        else:
            return render(request, 'novo_servico.html', {'form', form} )
        
def listar_servico(request):
    if request.method == "GET":
        servicos = Servicos.objects.all()
        return render(request, 'listar_servico.html', {'servicos': servicos})

def servico(request, identificador):
    servico = get_object_or_404(Servicos, identificador=identificador)
    return render(request, 'servico.html', {'servico': servico})

    