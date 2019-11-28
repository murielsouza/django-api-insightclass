from django.shortcuts import render
from django.http import HttpResponse
from api.models import *

def getListaClassificacao(request):
    listaAlunos = Aluno.objects.all()
    listaFrequencia = Frequencia.objects.all()
    listaTrabalhos = Trabalho.objects.all()
    notaTemp = 0;
    for a in listaAlunos:
        for f in listaFrequencia:
            if f.aluno.id == a.id:
                if f.aula1:
                    notaTemp = notaTemp + 150
                if f.aula2:
                    notaTemp = notaTemp + 150
        for t in listaTrabalhos:
            if t.aluno.id == a.id:
                notaTemp = notaTemp + t.nota*100
        for m in Missao.objects.all():
            if m.conclusao == "Concluída":
                notaTemp = notaTemp + m.valor
        Aluno.objects.filter(id=a.id).update(media=notaTemp)
        notaTemp = 0
    listaAlunos = Aluno.objects.order_by('-media')
    cont = 0
    for aluno in listaAlunos:
        cont+=1
        Aluno.objects.filter(id = aluno.id).update(posicao = cont)
    return HttpResponse(True)
