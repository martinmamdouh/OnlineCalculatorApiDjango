
from django.urls import path,include

from . import views
urlpatterns = [
    path('download/', views.export_history_to_xlsx),
]