"""insightclass_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers, serializers, viewsets
from api.views import *
from api.funcoes import getListaClassificacao

router = routers.DefaultRouter()
router.register(r'trofeis', TrofeuViewSet)
router.register(r'alunos', AlunoViewSet)
router.register(r'missoes', MissaoViewSet)
router.register(r'frequencias', FrequenciaViewSet)
router.register(r'trabalhos', TrabalhoViewSet)
router.register(r'classificacoes', ClassificacaoViewSet)
#router.register(r'turmas-salvar', SalvaTurmaViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^gerarclassificacao/', getListaClassificacao, name="Classificacao"),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
