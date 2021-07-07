from django.shortcuts import redirect,render
from .models import Usuario
from .forms import UsuarioForm

# Create your views here.


def index(request):

    usuarios = Usuario.objects.all()
    
    
    return render(request, 'proveedores/index.html', context = {'datos': usuarios})


def crearusuario(request):
    if request.method == 'POST':
        usuarioForm = UsuarioForm(request.POST, files=request.FILES)
        if usuarioForm.is_valid():
            usuarioForm.save()
            return redirect('crearusuario')
    else:
        usuarioForm=UsuarioForm()
    return render(request, 'proveedores/crearusuario.html', {'usuario': usuarioForm})


def ver(request):
    usuarios = Usuario.objects.all()
    return render(request, 'proveedores/ver.html', context={'usuarios': usuarios})
    


def form_mod_usuario(request,id):
    usuario = Usuario.objects.get(numId=id)

    datos={
        'form': UsuarioForm(instance=usuario)
    
    }
    if request.method == 'POST':
        formulario = UsuarioForm(data=request.POST, instance = usuario, files=request.FILES)
        if formulario.is_valid:
            formulario.save()
            return redirect('ver')
    return render(request, 'proveedores/form_mod_usuario.html', datos)




def form_del_usuario(request,id):
    usuario = Usuario.objects.get(numId=id)
    usuario.delete()
    return redirect('ver')



""" def metodo(numId, nombre, pais, fono):
    subcadena1 = numId [:2]
    print("Imprimiendo los dos primeros caracteres: " + subcadena1)
    subcadena2 = nombre[:2].upper()
    print("Imprimiendo los 2 primeros caracteres en mayúscula: " +subcadena2)
    subcadena3 = pais [-2:]
    print("Imprimiendo los dos últimos caracteres: " + subcadena3)
    subcadena4 = str(fono)[:2]
    print(subcadena4)
    cadenaUnida= subcadena1+subcadena2+subcadena3+subcadena4
    print("Imprimiendo cadena unida: " + cadenaUnida) """
    


""" a="Prueba"
b="Probando"
numero=123
print("Cadena de datos: " + a)
print("Otra cadena de datos: " + b)
metodo(a,b,numero) """

