from django.http import HttpResponse

from datetime import datetime

def hello_world(request):

    now = datetime.now().strftime('%b %dth,%Y - %H:%M hrs')# %b es el mes abreviado, %d es el dia, %Y es el año, %H es la hora, %M es el minuto, %S es el segundo
    return HttpResponse('Oh, hi! Current server time is {now}'.format(now=str(now)))


def hi(request):
    """Hi."""

    #import pdb; pdb.set_trace() # Esto es un breakpoint para debuggear
    print(request.GET['numbers'])
    return HttpResponse('Hi!')