from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('new-product/', views.AddProduct.as_view(), name='new_product'),
    path('product/<int:pk>/', views.ProductDetail.as_view(), name='product_detail'),
    path('product/<int:pk>/update', views.ProductUpdate.as_view(), name='product_update'),
    path('product/<int:pk>/delete', views.ProductDelete.as_view(), name='product_delete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    # urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
