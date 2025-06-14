
from django.contrib import admin
from django.urls import path, include

from django.conf.urls.static import static


from django.urls import re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


# TokenObtainPairView and TokenRefreshView views:
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


from config import settings

schema_view = get_schema_view(
    openapi.Info(
        title="Film API",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="ccvaf0803@gmail.com"),
        license=openapi.License(name="No License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)



urlpatterns = [
    path('admin/', admin.site.urls),
    # path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    #jwt
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    #include
    path('accountt/', include('account.urls')),
    path('user', include('user.urls')),
    path('maqola/', include('maqola.urls')),
    path('jurnal/', include('jurnal.urls')),
    # path('accounts/', include('django.contrib.auth.urls'))
]


urlpatterns += static(settings.STATIC_URL, document_rool=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_rool=settings.MEDIA_ROOT)
