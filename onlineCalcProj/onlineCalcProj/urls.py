
from django.contrib import admin
from django.urls import path,include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from rest_framework_swagger.views import get_swagger_view
schema_view = get_swagger_view(title='MegaSoft API')

#-------------------------
#from rest_framework.schemas import get_schema_view
#from rest_framework_swagger import renderers
#schema_view = get_schema_view(title="Fbs Api Docs", public=True, renderer_classes=[renderers.OpenAPIRenderer, renderers.SwaggerUIRenderer])
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('megasoft/api/v1.0/', include('basicCalc.urls')),
    path('megasoft/export/', include('exportHistory.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('megasoft/api/v1.0/docs', schema_view),
]
