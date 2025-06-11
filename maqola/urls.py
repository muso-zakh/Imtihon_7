from django.urls import path

from rest_framework.routers import DefaultRouter

from .views import MaqolaViewSet, last_peper, most_reads


router = DefaultRouter()

router.register(r'', MaqolaViewSet)

urlpatterns = [
    path('last_peper', last_peper),
    path('most_reads', most_reads)
]

urlpatterns += router.urls

