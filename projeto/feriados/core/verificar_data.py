from datetime import datetime
from django.shortcuts import render


def verificar_data(request):
    if request.method == 'POST':
        data = datetime.strptime(request.POST.get('data', ''), '%Y-%m-%d').date()
        if data.month == 12 and data.day == 25:
            mensagem = 'É Natal'
        elif data.month == 4 and data.day == 21:
            mensagem = 'É Tiradentes'
        elif data.month == 12 or data.month == 4:
            mensagem = 'É um mas não outro'
        else:
            mensagem = 'Hoje não é um dia especial'
        contexto = {'mensagem': mensagem}
        return render(request, 'verificar_data.html', contexto)
    else:
        return render(request, 'verificar_data.html')
