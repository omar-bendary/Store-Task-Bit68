from django.urls import path
from rest_framework_nested import routers
from .views import ProductList, CartViewSet, CartItemViewSet, OrderViewSet

urlpatterns = [
    path('products/', ProductList.as_view()),
]

router = routers.DefaultRouter()
router.register('carts', CartViewSet)
router.register('orders', OrderViewSet, basename='orders')


carts_router = routers.NestedDefaultRouter(router, 'carts', lookup='cart')
carts_router.register('items', CartItemViewSet, basename='cart-items')


# URLConf
urlpatterns += router.urls + carts_router.urls
