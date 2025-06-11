from django.shortcuts import render
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from rest_framework import viewsets, permissions
from rest_framework.response import Response

from .models import Maqola
from .serializers import MaqolaSerializer

from rest_framework import filters

from drf_yasg import openapi

from rest_framework.decorators import api_view, permission_classes
from drf_yasg.utils import swagger_auto_schema
 

class MaqolaViewSet(viewsets.ModelViewSet):
    queryset = Maqola.objects.filter(status=True)
    serializer_class = MaqolaSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    search_fields = ['title', 'author', 'id']

    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'author', 'maqola'] 


    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                'search',
                openapi.IN_QUERY,
                description="Search by title, author, maqola",
                type=openapi.TYPE_STRING
            )
        ]
    )

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.view_count += 1  
        instance.save(update_fields=['view_count'])  
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
    
    # @swagger_auto_schema(manual_parameters=[
    #     openapi.Parameter('title', openapi.IN_QUERY, description='title', type=openapi.TYPE_STRING),
    # ])

    # def list(self, request, *args, **kwargs):
    #     return super().list(request, *args, **kwargs)


    # def get_queryset(self):
    #     queryset = Maqola.objects.filter(status=True)
    #     title = self.request.GET.get('title')


    #     if title:
    #         queryset = queryset.filter(title=title)
            
    #     return queryset

@swagger_auto_schema(method='get', response={200: MaqolaSerializer})
@api_view(['GET'])
def last_peper(request):
    maqola = Maqola.objects.filter(status=True).order_by('-created_at')[:4]

    if maqola is None:
        return Response({"detail": "Hech qanday Maqola topilmadi."}, status=404)

    serializer = MaqolaSerializer(maqola, many=True)
    return Response(serializer.data)


@swagger_auto_schema(method='get', response={200: MaqolaSerializer})
@api_view(['GET'])
def most_reads(request):
    maqola = Maqola.objects.filter(status=True).order_by('view_count')[:5]

    if maqola is None:
        return Response({"detail": "Hech qanday Maqola topilmadi."}, status=404)

    serializer = MaqolaSerializer(maqola, many=True)
    return Response(serializer.data)

