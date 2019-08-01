
from django.contrib import admin
from django.urls import path,include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('megasoft/api/v1.0/', include('basicCalc.urls')),
]
