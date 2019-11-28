
from django.db import models
from django.contrib.auth.models import User
from django import forms

class Trofeu(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=128)
    descricao = models.TextField()
    CATEGORIA_CHOICES = (
        ('Bronze', 'Bronze'),
        ('Prata', 'Prata'),
        ('Ouro', 'Ouro'),
        ('Diamante', 'Diamante'),
        ('Lenda', 'Lendária')
    )
    categoria = models.CharField(max_length=8, choices=CATEGORIA_CHOICES, blank=False, null=False)
    img = models.TextField(null=True);

    def __str__(self):
        return str(self.id) +" | "+ self.nome + "(" + self.descricao+ ")" + self.categoria


class Aluno(models.Model):
    id = models.AutoField(primary_key=True)
    posicao = models.IntegerField(blank=True, null = True)
    nome = models.CharField(max_length=128)
    media = models.DecimalField(max_digits=6, decimal_places=2)
    trofeis = models.ManyToManyField(Trofeu, blank=True, related_name='trofeis')
    # usuario = models.ManyToManyField(User, blank=True, related_name='usuarios')
    #trofeis = models.CharField(max_length=256)
    #trabalhos = models.CharField(max_length=256)


    def __str__(self):
        return str(self.id) +" | " + self.nome + ", com pontuação de: " + str(self.media)

class Missao(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=128)
    descricao = models.TextField()
    CONCLUIDA_CHOICES = (
        ('Pendente', 'Pendente'),
        ('Concluída', 'Concluída'),
        ('Inconcluída', 'Inconcluída')
    )
    conclusao = models.CharField(max_length=12, choices=CONCLUIDA_CHOICES, blank=False, null=False)
    valor = models.IntegerField()

    def __str__(self):
        return str(self.id) +" | "+self.nome + "(" + self.descricao+ ")"

class Frequencia(models.Model):
    id = models.AutoField(primary_key=True)
    data = models.DateField(blank=False, null=True)
    aula1 = models.BooleanField(default = False)
    aula2 = models.BooleanField(default=False)
    aluno = models.ForeignKey(Aluno, null=True, blank=False, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id) +" | "+str(self.data) + "(" + str(self.aula1) + " - " + str(self.aula2) + ")" + "aluno: " + self.aluno.nome

class Trabalho(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=128)
    prazo = models.DateField(blank=False, null=True)
    valor = models.DecimalField(max_digits=4, decimal_places=2)
    nota = models.DecimalField(max_digits=4, decimal_places=2)
    isFeito = models.BooleanField(default=False)
    TIPO_CHOICES = (
        ('WEBAtividade', 'WEB-Atividade'),
        ('Prova', 'Prova'),
        ('Teste', 'Teste'),
        ('Relatório', 'Relatório'),
        ('Trabalho', 'Trabalho'),
        ('Outros', 'Outros')
    )
    tipo = models.CharField(max_length=14, choices=TIPO_CHOICES, blank=False, null=False)

    CATEGORIA_CHOICES = (
        ('G1', 'Grau 1'),
        ('G2', 'Grau 2')
    )
    categoria = models.CharField(max_length=2, choices=CATEGORIA_CHOICES, blank=False, null=False)
    aluno = models.ForeignKey(Aluno, null=True, blank=False, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id) +" | "+ self.nome + self.tipo + "(" + str(self.isFeito)+ ")" + self.categoria + "[" + self.aluno.nome + "]"

class Classificacao(models.Model):
    posicao = models.IntegerField()
    aluno = models.ForeignKey(Aluno, null=True, blank=False, on_delete=models.CASCADE)
    pontuacao = models.DecimalField(max_digits=6, decimal_places=2)
