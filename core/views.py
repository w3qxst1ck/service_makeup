import datetime

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
import json

from pytz import UTC

from core.models import Service, Category, Record


def home(request):
    return render(request, 'core/home.html')


def pricing(request):
    categories = Category.objects.all()
    context = {'categories': categories}
    return render(request, 'core/pricing.html', context)


def service_list(request, category_slug):
    categories = Category.objects.all()
    category = get_object_or_404(Category, slug=category_slug)
    context = {'categories': categories, 'category': category}
    return render(request, 'core/services.html', context)


def service(request, category_slug, id, slug):
    category = get_object_or_404(Category, slug=category_slug)
    service = get_object_or_404(Service, id=id, slug=slug)
    now = datetime.datetime.now()

    dates = [now + datetime.timedelta(days=i) for i in range(7)
            if (now + datetime.timedelta(days=i)).weekday() not in [5, 6]]
    times = ['0' + str(i) if len(str(i)) == 1 else str(i) for i in range(8, 18)]
    # ordered_times = [str(record.date.time())[:2] for record in Record.objects.filter(service__slug=slug,
    #                                                     date__gte=(now-datetime.timedelta(hours=now.hour)))]
    # ordered = {}
    # for rec in Record.objects.filter(service__slug=slug, date__gte=(now-datetime.timedelta(hours=now.hour))):
    #     if rec.date.day not in ordered:
    #         ordered[rec.date.day] = [str(rec.date.time())[:2]]
    #     else:
    #         ordered[rec.date.day].append(str(rec.date.time())[:2])
    # print(ordered)

    week = []
    for day in range(now.day, now.day + 1):
        for hour in range(8, 18):
            if datetime.datetime(now.year, now.month, day, hour).weekday() not in [5, 6]:
                week.append(datetime.datetime(now.year, now.month, day, hour, 0, 0, 0, UTC))

    ordering_dates = [rec.date for rec in Record.objects.filter(service__slug=slug,
                                                                date__gte=(now-datetime.timedelta(hours=now.hour)))]


    context = {'service': service, 'category': category, 'week': week, 'dates': dates, 'times': times}
    return render(request, 'core/services_in_category.html', context)


@login_required
def add_record(request):
    data = json.loads(request.body)
    year, month, day, hour = data['year'], data['month'], data['day'], data['hour']
    service_id = data['service']
    service = Service.objects.get(id=service_id)
    date = datetime.datetime(int(year), int(month), int(day), int(hour))
    if not Record.objects.filter(service=service_id, date=date):
        Record.objects.create(user=request.user, service=service, date=date)

    return JsonResponse('Record was added', safe=False)






