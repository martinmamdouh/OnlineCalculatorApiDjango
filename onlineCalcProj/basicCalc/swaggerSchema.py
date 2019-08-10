
from rest_framework_swagger.renderers import OpenAPIRenderer, SwaggerUIRenderer
from rest_framework.filters import BaseFilterBackend
import coreapi

class SimpleFilterBackend(BaseFilterBackend):

  
       def get_schema_fields(self, view):
              return [coreapi.Field(
                  name='expression',
                  location='query',
                  required=True,
                  type='string',          
              )]
