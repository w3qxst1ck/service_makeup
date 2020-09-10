from django.shortcuts import render, get_object_or_404

from core.models import Service, Category


def home(request):
    return render(request, 'core/home.html')


def pricing(request):
    categories = Category.objects.all()
    context = {'categories': categories}
    return render(request, 'core/pricinghtml', context)


def service_list(request, category_slug):
    categories = Category.objects.all()
    services = Service.objects.all()
    category = get_object_or_404(Category, slug=category_slug)
    context = {'services': services, 'categories': categories, 'category': category}
    return render(request, 'core/services.html', context)
