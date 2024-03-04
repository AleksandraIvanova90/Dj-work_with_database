from django.shortcuts import render, redirect

from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    if request.GET.get('sort') == 'name':
        context = {
            'phones': Phone.objects.all().order_by('name')
        }
        return render(request, template, context)
    elif request.GET.get('sort') == 'min_price':
        context = {
            'phones': Phone.objects.all().order_by('price')
        }
        return render(request, template, context)
    elif request.GET.get('sort') == 'max_price':
        context = {
            'phones': Phone.objects.all().order_by('-price')
        }
        return render(request, template, context)
    else:
        context = {
            'phones': Phone.objects.all()
        }
        return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    context = {
        'phone': Phone.objects.filter(slug__contains=slug).first()

    }
    return render(request, template, context)
