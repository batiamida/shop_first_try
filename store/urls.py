from django.urls import path
from . import views

urlpatterns = [
	path('', views.products_page, name = 'products_page'),
	path('shop_page/', views.shop, name='shop'),
	path('single_item/<int:pk>/', views.single_item, name='single_item'),
	
]