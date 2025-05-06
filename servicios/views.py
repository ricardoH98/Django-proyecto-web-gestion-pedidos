from django.shortcuts import render
from servicios.models import Servicio
# Create your views here.

def servicios(request):
    print('el request es: ',request)
    print(type(request))
    servicios = Servicio.objects.all()
    return render(request, 'servicios/servicios.html', {'servicios': servicios})
