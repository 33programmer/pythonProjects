from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from .models import Appointments
import json
from django.core import serializers
# Create your views here.


def index(request):
    submitted = "Not submitted"
    if request.method == 'POST':
        time = request.POST.get('time')
        day = request.POST.get('day')
        description = request.POST.get('description')

        Appointments.objects.create(
            time=time,
            day=day,
            description=description
        )
        submitted = "Submitted"

    context = {'response': submitted}
    return render(request, 'index.html', context)


def search(request):
    query = request.GET.get('search_value', None)
    if query == '':
        data = Appointments.objects.all()
    else:
        data = Appointments.objects.filter(description__icontains=query)

    try:
        data = serializers.serialize('json', data)
        print "Found the query!"
    except ValueError:
        print "Something is wrong with the URL variables"

    context = {'data': data}

    return JsonResponse(context)

