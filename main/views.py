from django.http import HttpResponse
from django.shortcuts import render


def index(request) -> HttpResponse:
    context = {
        'title': 'DECOROOM - главная страница',
        'content': 'DECOROOM ',
    }
    return render(request, 'main/index.html', context)


def about(request) -> HttpResponse:
    context = {
        'title': 'DECOROOM - о нас',
        'content': 'о нас',
        'text_on_page': 'Добро пожаловать в DECOROOM! Мы - команда энтузиастов и профессионалов,'
                        ' объединенных страстью к созданию пространства, '
                        'в котором ваш дом становится истинным отражением вашего стиля и уюта. В'
                        ' DECOROOM мы стремимся предложить вам не просто мебель, а настоящие истории,'
                        ' переплетенные с вашими собственными моментами радости и комфорта. Мы верим, что каждый дом'
                        ' уникален, и мебель - это не просто предметы, а часть вашей идентичности. Наша миссия - помочь вам '
                        'обустраивать ваш дом так, чтобы он не только соответствовал вашему стилю, но и олицетворял ваши жизненные'
                        ' ценности. Мы гордимся тем, что предлагаем качественную мебель, которая прослужит вам долгие годы, принося '
                        'радость и уют в каждый уголок вашего дома.'
    }
    return render(request, 'main/about.html', context)


def contacts(request) -> HttpResponse:
    context = {
        'title': 'DECOROOM - наши контакты',
        'content': 'Наши контакты:',
        'text_address': 'Проезд Диванний, 45,  г. Папакарловськ, Кресловсько-Диванная область',
        'tel_number': '+3(456)789-00-00',
        'email': 'dtakov13@gmail.com',
        'shedule': 'Без перерыва и выходных'
    }
    return render(request, 'main/contacts.html', context)


def delivery(request) -> HttpResponse:
    context = {
        'title': 'DECOROOM - доставка и оплата',
        'content': 'DECOROOM - доставка и оплата:',
        'tel_number': '+3(456)789-00-00',
        'email': 'dtakov13@gmail.com',
        'delivery_text': 'Без перерыва и выходных'
    }
    return render(request, 'main/delivery.html', context)
