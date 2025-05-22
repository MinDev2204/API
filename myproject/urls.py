from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from myapp.views import UserViewSet, ProductViewSet, CategoryViewSet
from django.conf import settings
from django.conf.urls.static import static

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'products', ProductViewSet)
router.register(r'categories', CategoryViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]

# Media fayllar uchun
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
