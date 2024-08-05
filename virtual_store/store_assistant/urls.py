from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('product_location/<int:product_id>/', views.product_location, name='product_location'),
    path('category/<str:category>/', views.category_products, name='category_products'),
    path('contact_us/', views.contact_us, name='contact_us'),
    path('login/', views.login, name='login'),
    path('view_details/<int:product_id>/', views.view_details, name='view_details'),
    path('ar_view/', views.ar_view, name='ar_view'),
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('view_cart/', views.view_cart, name='view_cart'),
    path('update_cart_quantity/<int:product_id>/<str:action>/', views.update_cart_quantity, name='update_cart_quantity'),
    path('remove_from_cart/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'), 
    path('customer_id/', views.customer_id, name='customer_id'),
    path('recommendations', views.recommendations, name='recommendations'),
    path('payments/', views.payments, name='payments'),
    path('checkout/', views.checkout, name='checkout'),
    path('checkout_success/', views.checkout_success, name='checkout_success'),
    path('categories/', views.categories, name='categories'),
]
