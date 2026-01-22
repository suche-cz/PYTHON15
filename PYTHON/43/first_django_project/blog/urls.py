from django.urls import path
from django.http import HttpResponse
from django.shortcuts import render


def my_page(request):
    import datetime as dt
    import time

    now = dt.datetime.now()
    # time.sleep(3)

    return HttpResponse(f'<h1>Current datetime is: {now}</h1>', headers={'X-data': 1212})


def my_html(request):
    data = {'name': 'Suche', 'date': '1988-01-12'}
    return render(request, 'blog/my_html.html')


def random_password(request):
    from django.utils.crypto import get_random_string, RANDOM_STRING_CHARS

    length = int(request.GET.get('length', 12))
    letters = request.GET.get('letters')
    numbers = request.GET.get('numbers')
    symbols = request.GET.get('symbols')

    allowed_chars = ''

    if letters:
        allowed_chars += 'abcedfgh'
    if numbers:
        allowed_chars += '0123456789'
    if symbols:
        allowed_chars += '$._!-'
    
    allowed_chars = allowed_chars or RANDOM_STRING_CHARS

    random_pass = get_random_string(length=length, allowed_chars=allowed_chars)
    
    return render(request, 'blog/random_password.html', {
        'password': random_pass,
        'length': length,
        'letters': letters,
        'numbers': numbers,
        'symbols': symbols,
    })


def get_name_length(request):
    """
    1. napojit view na path - ok
    2. nastavit vstupní parametry pro view
    3. vykreslit template pomocí render
    4. otestovat že stránka funguje na dané adrese
    5. vytvořit tam formulař s políčkem pro zadání jména
    6. ve view získat data z foruláře
    7. vypočet počtu znaků
        pokud je zadané jméno -> může se vypočítat počet znaků
        jinak nastavím počet na ''
    """
    name = request.GET.get('name', '')
    if name:
        length = len(name)
    else:
        length = ''

    return render(request, 'blog/name-length.html', {'length': length, 'name': name})


urlpatterns = [
    path('my-page/', my_page),
    path('my-html/', my_html),
    path('random-password/', random_password),
    path('get-name-length/', get_name_length),
]
