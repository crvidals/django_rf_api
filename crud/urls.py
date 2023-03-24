from rest_framework import routers
from .api import EmpresasViewSet, PersonasViewSet

router = routers.DefaultRouter()

router.register('api/empresas', EmpresasViewSet, 'empresas')
router.register('api/personas', PersonasViewSet, 'personas')

urlpatterns = router.urls