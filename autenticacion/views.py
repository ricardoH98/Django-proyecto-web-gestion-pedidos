from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

# Create your views here.

class VRegistro(View):

    def get(self, request):
        form = UserCreationForm()

        return render(request, 'registro.html', {'form': form})

    def post(self, request):
        form = UserCreationForm(request.POST)
        
        if form.is_valid():
            usuario = form.save() # Registro del usuario en la base de datos
            login(request, usuario) # Mantenemos la sesión iniciada con el usuario que acabamos de registrar
            
            return redirect('Home')
        
        else:

            # Muestra en el formulario todos los errores por no cumplir con los requisitos
            for msg in form.error_messages: 
                messages.error(request, form.error_messages[msg])

            return render(request, 'registro.html', {'form': form})
        
def cerrar_sesion(request):
    logout(request)

    return redirect('Home')

def logear(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data= request.POST)
        if form.is_valid():
            nombre_usuario = form.cleaned_data.get('username')
            contrasena = form.cleaned_data.get('password')
            usuario = authenticate(username = nombre_usuario, password= contrasena)
            # print('el usuario es: ',usuario)
            if usuario is not None:
                login(request, usuario)
                return redirect('Home')
            else:
                messages.error(request, 'usuario no válido')
        else:
            messages.error(request, 'información incorrecta')

    form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})
