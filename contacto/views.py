from django.shortcuts import render, redirect
from .forms import FormularioContacto
from django.core.mail import EmailMessage
# Create your views here.
def contacto(request):
    formulario_contacto = FormularioContacto()

    if request.method == 'POST':
        formulario_contacto = FormularioContacto(data=request.POST)
        if formulario_contacto.is_valid():
            nombre = request.POST.get('nombre')
            email = request.POST.get('email')
            contenido = request.POST.get('contenido')

            email = EmailMessage(
                subject='Mensaje desde App Django',
                body=f'El usuario con nombre {nombre} con la dirección {email} escribe lo siguiente:\n\n {contenido}',
                from_email='',
                to=['ricardo060498@gmail.com'],
                reply_to=[email]
            )

            try:
                email.send()
                return redirect('/contacto/?valido')
            
            except:
                return redirect('/contacto/?novalido')


    return render(request, 'contacto.html', {'mi_formulario': formulario_contacto})