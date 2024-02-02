from django.urls import path 

from . import views 


urlpatterns = [
    path('detail/', views.product_list_view), 
    path('create/', views.product_create_view), 
    path('<int:pk>',views.product_detail_view),
    path('<int:pk>/update/',views.product_update_view), 
    path('<int:pk>/delete/',views.product_delete_view), 
]