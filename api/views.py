from django.shortcuts import render
from rest_framework import routers, serializers, viewsets
from django.http import HttpResponse
from django.contrib.auth.models import User
from api.models import *
from api.serializers import *


class TrofeuViewSet(viewsets.ModelViewSet):
    queryset = Trofeu.objects.all()
    serializer_class = TrofeuSerializer

class AlunoViewSet(viewsets.ModelViewSet):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer

class MissaoViewSet(viewsets.ModelViewSet):
    queryset = Missao.objects.all()
    serializer_class = MissaoSerializer

class FrequenciaViewSet(viewsets.ModelViewSet):
    queryset = Frequencia.objects.all()
    serializer_class = FrequenciaSerializer

class TrabalhoViewSet(viewsets.ModelViewSet):
    queryset = Trabalho.objects.all()
    serializer_class = TrabalhoSerializer

class ClassificacaoViewSet(viewsets.ModelViewSet):
    queryset = Classificacao.objects.all()
    serializer_class = ClassificacaoSerializer
