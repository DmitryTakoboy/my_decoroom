from django.http import HttpResponse
from django.shortcuts import render


def index(request) -> HttpResponse:

    context = {
        'title': 'home - главная страница',
        'content': 'Магазин мебели HOME',
    }
    return render(request, 'main/index.html', context)


def about(request) -> HttpResponse:
    context = {
        'title': 'home - о нас',
        'content': 'о нас',
        'text_on_page': 'Tаковой создает магазин по урокам из интернета но могу и продать старый Степанський диван'
    }
    return render(request, 'main/about.html', context)
