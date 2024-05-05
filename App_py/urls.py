from django.urls import path
from . import views
urlpatterns =[
     path('Marksrequest/',views.MarksResponse),
     path('ResultRequest/',views.Resultresponse)
]