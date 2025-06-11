from django.urls import path

from rest_framework.routers import DefaultRouter

from .views import JurnalViewSet, last_edition


router = DefaultRouter()

router.register(r'', JurnalViewSet)

urlpatterns = [
    path('last_edition', last_edition)
]

urlpatterns += router.urls

