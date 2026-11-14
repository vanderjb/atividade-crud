from django import forms
from .models import Funcionario


# formulario do funcionario (as views usam o model direto,
# mas deixei aqui caso precise personalizar depois)
class FuncionarioForm(forms.ModelForm):
    class Meta:
        model = Funcionario
        fields = "__all__"
