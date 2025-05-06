from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import send_mail
from carro.carro import Carro
from django.contrib import messages
from .models import LineaPedido, Pedido

# Create your views here.

@login_required(login_url='/autenticacion/logear')
def procesar_pedido(request):
    pedido = Pedido.objects.create(user= request.user)
    carro = Carro(request)
    # print(pedido.total)
    lineas_pedidos = list()
    for key, value in carro.carro.items():
        lineas_pedidos.append(LineaPedido(
            producto_id = key,
            cantidad = value['cantidad'],
            user = request.user,
            pedido_id = pedido.id
        ))

    LineaPedido.objects.bulk_create(lineas_pedidos)
    print(lineas_pedidos)
    enviar_mail(
        pedido = pedido,
        lineas_pedidos = lineas_pedidos,
        nombreusuario = request.user.username,
        emailusuario = request.user.email
    )

    messages.success(request, 'El pedido se ha creado correctamente')

    return redirect('Tienda')

def enviar_mail(**kwargs):
    asunto = 'Gracias por el pedido'
    mensaje = render_to_string(
        'pedido.html',
        {
            'pedido': kwargs.get('pedido'),
            'lineas_pedidos': kwargs.get('lineas_pedidos'),
            'nombreusuario': kwargs.get('nombreusuario'),
            'emailusuario': kwargs.get('emailusuario')
        }
    )

    mensaje_texto = strip_tags(mensaje)
    from_email = 'correodepruebas9829@gmail.com'
    to=kwargs.get('emailusuario')
    # to = 'ricardo060498@gmail.com'
    send_mail(asunto, mensaje_texto, from_email, [to], html_message=mensaje)

