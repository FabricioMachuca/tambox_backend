from rest_framework import routers

from .views import ProductsView

router = routers.SimpleRouter()
router.register(r'products', ProductsView, basename='products')
urlpatterns = router.urls