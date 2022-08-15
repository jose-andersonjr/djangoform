from socket import fromshare
from django import forms


SEXO_CHOICES = (
    ('M', 'Masculino'),
    ('F', 'Feminino')
)

class MeuFormulario(forms.Form):
    nome = forms.CharField(max_length=30)
    sexo = forms.ChoiceField(choices=SEXO_CHOICES)
    email = forms.EmailField(required=False)
    data_nascimento = forms.DateField(required=False)
