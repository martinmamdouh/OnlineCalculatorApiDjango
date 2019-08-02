
from django.contrib import admin
from django.urls import path,include

from rest_framework_swagger.views import get_swagger_view
schema_view = get_swagger_view(title='MegaSoft API')
urlpatterns = [
    path('admin/', admin.site.urls),
    path('megasoft/api/v1.0/', include('basicCalc.urls')),
    path('megasoft/api/v1.0/docs', schema_view),
    path('megasoft/export/', include('exportHistory.urls')),
]
