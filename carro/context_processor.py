def importe_total_carro(request):
    total = 0
    # try:
    # if request.user.is_authenticated:
    try:
        for key, value in request.session['carro'].items():
            total = total + float(value['precio'])
    except:
        print('error')
        
    return {'importe_total_carro': total}