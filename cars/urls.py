from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from rest_framework import routers
from cars import views

router = routers.DefaultRouter()
router.register(r'cars', views.CarsView, 'car')

urlpatterns = [
    path('', include(router.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)