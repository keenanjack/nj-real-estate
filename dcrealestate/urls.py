from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'propertysearch', views.property_data),
    url(r'propertytypes', views.property_types)
]