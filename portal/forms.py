from django.forms import ModelForm, TextInput
from django.utils.translation import gettext_lazy as _
from .models import Datosclientes


class ClientForm(ModelForm):
    class Meta:
        model = Datosclientes
        fields = '__all__'
        labels = {
            'Title': _('Cliente'),
            'Docnro': _('RUC/DNI/CI/RG'),
            'telefono': _('Teléfono'),
            'email': _('Correo electrónico'),
            'Direcc': _('Dirección'),
            'DireccFact': _('Dirección de facturación'),
            'Facturaranombrede': _('Facturar a nombre de'),
            'comprobantep': _('Comprobante de pago'),
        }
        widgets = {
            'Title': TextInput(attrs={'class':'form-control'}),
            'Docnro': TextInput(attrs={'class':'form-control'}),
            'telefono': TextInput(attrs={'class':'form-control'}),
            'email': TextInput(attrs={'class':'form-control'}),
            'Direcc': TextInput(attrs={'class':'form-control'}),
            'DireccFact': TextInput(attrs={'class':'form-control'}),
            'Facturaranombrede': TextInput(attrs={'class':'form-control'}),
        }


















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

    
    

 