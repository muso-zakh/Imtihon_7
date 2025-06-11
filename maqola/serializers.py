from rest_framework.serializers import ModelSerializer

from .models import Maqola
  


class MaqolaSerializer(ModelSerializer):
    class Meta:
        model = Maqola
        fields = '__all__'
        read_only_fields =  ('id', 'created_at', 'view_count', 'status') 
