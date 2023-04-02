from datetime import datetime
from django.shortcuts import render

def mensagem_para_data_atual():
    hoje = datetime.now().date()
    if hoje.month == 12 and hoje.day == 25:
        return 'É Natal'
    elif hoje.month == 4 and hoje.day == 21:
        return 'É Tiradentes'
    else:
        return 'Hoje não é um dia especial'

def natal(request):
    contexto = {
        'mensagem': mensagem_para_data_atual() == 'É Natal'
    }
    return render(request, 'index.html', contexto)

def tiradentes(request):
    contexto = {
        'mensagem': mensagem_para_data_atual() == 'É Tiradentes'
    }
    return render(request, 'index.html', contexto)
