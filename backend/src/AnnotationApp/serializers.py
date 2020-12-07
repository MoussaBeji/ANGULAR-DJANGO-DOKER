from rest_framework import serializers
from .models import Labels


class LabelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Labels
        fields = ('LabelId',
                  'LabelName',
                  'Description',
                  'Color')
                  