from django.urls import path, include
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.prod_list, name = 'all_products'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('accounts.urls')),
    path('<uuid:category_id>/', views.prod_list, name = 'products_by_category'),
    path('<uuid:category_id>/<uuid:product_id>/', views.product_detail, name = 'product_detail'),
]
