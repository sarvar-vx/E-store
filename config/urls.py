from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from products.views import home_page, product_detail

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_page, name='home'),
    path('category/<slug:category_slug>/', home_page, name='category_filter'),
    path('product/<int:pk>/', product_detail, name='product_detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)