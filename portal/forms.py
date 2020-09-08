from django.forms import ModelForm
from .models import Datosclientes


class ClientForm(ModelForm):
    class Meta:
        model = Datosclientes
        fields = '__all__'


















""" class PostForm(forms.Form):

    Title = forms.CharField(label='Cliente', max_length=20, widget=forms.TextInput(attrs={
        'class':'form-control', 'placeholder': 'Cliente',
    }))
    Direcc = forms.CharField(label='Direccion', max_length=35, widget=forms.TextInput(attrs={
        'class':'form-control', 'placeholder': 'Dirección',
    }))
    DireccFact = forms.CharField(label='Dirección de facturación', max_length=40, widget=forms.TextInput(attrs={
        'class':'form-control', 'placeholder': 'Dir Facturacion',
    }))
    Facturaranombrede = forms.CharField(label='Facturar a nombre de', max_length=20, widget=forms.TextInput(attrs={
        'class':'form-control', 'placeholder': 'Fact a nombre de',
    })) """

    
    

 