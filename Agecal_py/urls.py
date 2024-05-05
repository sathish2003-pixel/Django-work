from django.urls import path
from . import views
urlpatterns=[
    path('home/',views.homepage),
    path('menu/',views.menupage),
    path('order/',views.menuorder)
]