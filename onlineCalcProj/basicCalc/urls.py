from django.urls import path
from . import views

urlpatterns = [

    path('calculate/', (views.OnlineCalculator.as_view())),
]
