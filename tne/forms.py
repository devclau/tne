from django import forms
from django.forms import ModelForm
from django.core import validators
from django.forms.widgets import RadioSelect, Select, CheckboxSelectMultiple
from tne.models import T_TNE_SOLICITUDES

class FormulatioTne(forms.Form):

    CHOICES = [('SI', 'SI'), ('NO', 'NO')]
    INSCRIPCION = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(attrs={'class':'form-check-input position-static', 'name':'INSCRIPCION'}))

    
    semestre_choices = [('', '----'),('1SEM', 'SEMESTRE 1'), ('2SEM', 'SEMESTRE 2'), ('AMBOS', 'AMBOS')]
    INSCRIPCION_PERIODO = forms.ChoiceField(required=False, choices=semestre_choices, widget=Select(attrs={'class':'form-control', 'name':'INSCRIPCION_PERIODO'}))

    CHOICES_TNE = [('REVALIDAR', 'Requiero revalidar su TNE para este año'), ('NUEVA', 'Requiero solicitar por primera vez la TNE para este año'), ('NO_REQUIERO', 'No requiero solicitar, o revalidar TNE para este año.')]
    TNE_SOLICITUD= forms.ChoiceField(choices=CHOICES_TNE, widget=forms.RadioSelect(attrs={'class':'form-check-input-chex', 'name':'TNE_SOLICITUD'}))


class FormularioLogin(forms.Form):
        email = forms.CharField(required=True, widget=forms.TextInput(
            attrs={'class':'form-control', 'placeholder': 'email@alumnos.ulagos.cl', 'autocomplete':'off', 'type':'text'}
            ),
        validators= [validators.MaxLengthValidator(8, message='El RUT supera los carcateres maximo')]
        )

        password = forms.CharField(required=True, widget=forms.PasswordInput(
            attrs={'class':'form-control', 'placeholder': 'Password', 'autocomplete':'off', 'type':'password'}
            ),
        validators= [validators.MaxLengthValidator(1, message='El digito verificador supera los carcateres maximo')]
        )


class FormularioRegistroTne(ModelForm):
    FECHA_SOLICITUD = forms.CharField(required=False)
    RUT = forms.CharField(required=True)
    PERIODO_SOLICITUD = forms.CharField(required=True)
    INSCRIPCION = forms.CharField(required=True)
    INSCRIPCION_PERIODO = forms.CharField(required=False)
    TNE_REVALIDAR = forms.CharField(required=True)
    TNE_NUEVO = forms.CharField(required=True)

    class Meta:
        model = T_TNE_SOLICITUDES
        fields = ['FECHA_SOLICITUD', 'RUT', 'PERIODO_SOLICITUD', 'INSCRIPCION','INSCRIPCION_PERIODO','TNE_REVALIDAR','TNE_NUEVO']
