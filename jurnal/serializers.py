from rest_framework.serializers import ModelSerializer

from .models import Jurnal
  


class JurnalSerializer(ModelSerializer):
    class Meta:
        model = Jurnal
        fields = '__all__'
        read_only_fields =  ('id', 'created_at', 'view_count', 'status') 
