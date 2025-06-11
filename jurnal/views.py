from django.shortcuts import render
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from rest_framework.response import Response
from rest_framework import viewsets, permissions

from .models import Jurnal
from .serializers import JurnalSerializer

from .pagination import JurnalPagination

from rest_framework.decorators import api_view, permission_classes
from drf_yasg.utils import swagger_auto_schema
 

class JurnalViewSet(viewsets.ModelViewSet):
    queryset = Jurnal.objects.all()
    serializer_class = JurnalSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    pagination_class = JurnalPagination

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.view_count += 1  
        instance.save(update_fields=['view_count'])  
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
    

@swagger_auto_schema(method='get', response={200: JurnalSerializer})
@api_view(['GET'])
def last_edition(request):
    jurnal = Jurnal.objects.order_by('-created_at').first()

    if jurnal is None:
        return Response({"detail": "Hech qanday jurnal topilmadi."}, status=404)

    serializer = JurnalSerializer(jurnal)
    return Response(serializer.data)