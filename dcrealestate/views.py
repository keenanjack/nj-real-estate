

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from .models import Properties, LandUse

def property_data(request):
    landusecode = request.GET['landusecode']
    min_val = request.GET['min_val']
    max_val = request.GET['max_val']
    all_properties = Properties.objects.filter(
        LAND_USE_CODE=landusecode).filter(
            APPRAISED_VALUE_CURRENT_TOTAL__gte=min_val).filter(
                APPRAISED_VALUE_CURRENT_TOTAL__lte=max_val).values()
    all_properties_list = list(all_properties)
    return JsonResponse(all_properties_list, safe=False)

def property_types(request):
    all_property_types = LandUse.objects.values()
    all_properties_types_list = list(all_property_types)
    return JsonResponse(all_properties_types_list, safe=False)

# Create your views here.
