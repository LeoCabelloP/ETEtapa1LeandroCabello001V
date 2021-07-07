from django import forms
from django.forms import ModelForm, widgets
from .models import Usuario


class UsuarioForm(ModelForm):
    """ Logo = forms.ImageField(required=False)  """
    
    class Meta:
 
        model = Usuario
        fields = ['numId', 'logoProveedor',
                  'nombre', 'fono', 'direccion',
                  'region', 'email', 'email2', 'pais',
                  'contrasenna', 'contrasenna2','moneda_pago']

        labels = {
            'numId': 'Número de Identificación',
            'logoProveedor': 'Ingrese su logo de proveedor',             
            'nombre': 'Nombre completo del proveedor (se recomienda incluir ambos apellidos)',
            'fono': 'Número de teléfono', 
            'direccion': 'Dirección',
            'region': 'Región',
            'email': 'Ingrese su email',
            'email2': 'Reingrese su email',
            'pais': 'País',
            'contrasenna': 'Ingrese su contraseña',
            'contrasenna2': 'Reingrese su contraseña',
            'moneda_pago': 'Moneda de pago (Pesos o Dólares)'
        }

        widgets = {
            'numId': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese su número de identificacion',
                    'id': 'numId'

                }
            ),
            
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese su nombre',
                    'id': 'nombre'
                }
            ),
            'fono': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese su número de teléfono',
                    'id': 'fono'
                }
            ),
            'direccion': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese su dirección',
                    'id': 'direccion'
                }
            ),
            'region': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese su región',
                    'id': 'region',
                }
            ),
            'email': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese su correo electrónico',
                    'id': 'email',
                    'type': 'email'
                }
            ),
            'email2': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese su correo electrónico',
                    'id': 'email',
                    'type': 'email'
                }
            ),
            'pais': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese su país',
                    'id': 'pais',
                }
            ),
            'contrasenna': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese su contraseña',
                    'id': 'contrasenna',
                    'type': 'password'
                }
            ),
            'contrasenna2': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Vuelva a ingresar su contraseña',
                    'id': 'contrasenna2',
                    'type': 'password'
                }
            ),
            'moneda_pago': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese su moneda de pago (Peso/Dólar)',
                    'id': 'moneda_pago'
                }
            ),

        }
