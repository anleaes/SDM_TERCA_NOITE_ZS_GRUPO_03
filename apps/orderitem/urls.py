from django.urls import path, include
from . import views
from rest_framework import routers


app_name = 'orderitem'

router = routers.DefaultRouter()
router.register('', views.OrderItemViewSet, basename='pedidos_itens')

urlpatterns = [
    path('', include(router.urls) )
]
