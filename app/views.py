from django.shortcuts import render
from django.views.generic import (
    CreateView, ListView, UpdateView, DetailView, DeleteView
)
from django.urls import reverse_lazy
from .models import Funcionario


# Create - cadastro de funcionario
class FuncionarioCreateView(CreateView):
    model = Funcionario
    fields = "__all__"
    template_name = "form_funcionario.html"
    success_url = reverse_lazy("lista_funcionarios")


# Read - lista com todos os funcionarios
class FuncionarioListView(ListView):
    model = Funcionario
    template_name = "lista_funcionarios.html"


# Update - usa o mesmo formulario do cadastro
class FuncionarioUpdateView(UpdateView):
    model = Funcionario
    fields = ("nome", "cpf", "email", "remuneracao")
    template_name = "form_funcionario.html"
    success_url = reverse_lazy("lista_funcionarios")


# Read - mostra os dados de um funcionario so
class FuncionarioDetailView(DetailView):
    model = Funcionario
    template_name = "lista_funcionario.html"
    context_object_name = "fun"


# Delete - remove o funcionario
class FuncionarioDeleteView(DeleteView):
    model = Funcionario
    template_name = "remover_funcionario.html"
    context_object_name = "fun"
    success_url = reverse_lazy("lista_funcionarios")
