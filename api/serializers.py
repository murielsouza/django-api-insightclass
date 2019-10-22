from rest_framework import routers, serializers, viewsets
from drf_writable_nested import WritableNestedModelSerializer
from django.contrib.auth.models import User
from api.models import Aluno, Missao, Trofeu, Frequencia, Trabalho, Classificacao


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')

class TrofeuSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Trofeu
        fields = ('id','nome', 'descricao', 'categoria', 'img')

class AlunoSerializer(WritableNestedModelSerializer):
    trofeis = TrofeuSerializer(many = True)
    class Meta:
        model = Aluno
        fields = ('id','nome', 'media','trofeis')

class MissaoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Missao
        fields = ('id','nome', 'descricao', 'conclusao', 'valor')

class FrequenciaSerializer(serializers.HyperlinkedModelSerializer):
    aluno = AlunoSerializer(many=False)
    class Meta:
        model = Frequencia
        fields = ('id','data', 'aula1', 'aula2', 'aluno')

class TrabalhoSerializer(serializers.HyperlinkedModelSerializer):
    aluno = AlunoSerializer(many=False)
    class Meta:
        model = Trabalho
        fields = ('id','nome','prazo', 'valor', 'nota', 'isFeito', 'tipo', 'categoria', 'aluno')

class ClassificacaoSerializer(serializers.HyperlinkedModelSerializer):
    aluno = AlunoSerializer(many=False)
    class Meta:
        model = Classificacao
        fields = ('posicao','aluno','pontuacao')
