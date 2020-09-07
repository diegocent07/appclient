from django import forms
from .models import Datosclientes

class PostForm(forms.Form):

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
    }))

    """ def registrar_datos(self):
        registro_datos = Datosclientes(Title=self.data['Title'],
        Direcc=self.data['Direcc'],
        DireccFact=self.data['DireccFact'],
        Facturaranombrede=self.data['Facturaranombrede'])
        registro_datos.save()
        return 'Registro de datos exitoso!' """
    
    

 