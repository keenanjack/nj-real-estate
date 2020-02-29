from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from .models import Municipalities

def property_locations(request):
    unique_counties = Municipalities.objects.values()
    unique_county_list = list(unique_counties)
    return JsonResponse(unique_county_list, safe=False)

# Create your views here.
