from django.core.paginator import Paginator
from django.db.models import ExpressionWrapper, DecimalField, F
from django.shortcuts import render, get_list_or_404

from goods.models import Products
from goods.utils import q_search


def catalog(request, category_slug=None):
    page = request.GET.get("page", 1)
    on_sale = request.GET.get("on_sale", None)
    order_by = request.GET.get("order_by", None)
    query = request.GET.get("q", None)

    if category_slug == "all":
        goods = Products.objects.all()
    elif query:
        goods = q_search(query)
    else:
        goods = get_list_or_404(Products.objects.filter(category__slug=category_slug))

    if on_sale:
        goods = goods.filter(discount__gt=0)

    if order_by and order_by != "default":
        if order_by == "price":
            goods = goods.annotate(discounted_price=ExpressionWrapper(
                F('price') - F('price') * F('discount') / 100.0,
                output_field=DecimalField()  # Указываем DecimalField
            )).order_by('discounted_price')
        elif order_by == "-price":
            goods = goods.annotate(discounted_price=ExpressionWrapper(
                F('price') - F('price') * F('discount') / 100.0,
                output_field=DecimalField()  # Указываем DecimalField
            )).order_by('-discounted_price')

    paginator = Paginator(goods, 3)
    current_page = paginator.page(page)

    context = {
        "title": "DECOROOM-Каталог",
        "goods": current_page,
        "slug_url": category_slug,
    }
    return render(request, 'goods/catalog.html', context)


def product(request, product_slug):
    product = Products.objects.get(slug=product_slug)
    context = {'product': product}

    return render(request, 'goods/product.html', context=context)
