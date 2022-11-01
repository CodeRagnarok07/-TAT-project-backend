from rest_framework import routers
from .views import PaginaView , SeccionView, ContenidoView

router = routers.DefaultRouter()

# page_list = PaginaView.as_view({'get': 'list'})
# page_detail = PaginaView.as_view({'get': 'retrieve'})


router.register(r'paginas', PaginaView, basename='paginas')
router.register('seccion', SeccionView)
router.register('sub-titulo', ContenidoView)

urlpatterns = router.urls