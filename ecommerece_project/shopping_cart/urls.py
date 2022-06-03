
from django.urls import path
from . import views
app_name='shopping_cart'

urlpatterns = [
    path('',views.allProdCart, name='allProdCart'),
    path('<slug:c_slug>/', views.allProdCart, name='product_by_category'),
    path('<slug:c_slug>/<slug:product_slug>/', views.proDetail, name='prodCatdetail')
]
