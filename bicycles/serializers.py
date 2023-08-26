from rest_framework import serializers
from .models import Bicycle


class BicycleSerializer(serializers.Serializer):
    type = serializers.CharField(max_length=120)
    make = serializers.CharField()
    model_name = serializers.CharField()
    year = serializers.IntegerField()
    id = serializers.IntegerField(read_only=True)
    

    def create(self, validated_data):
        return Bicycle.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.type = validated_data.get('type', instance.type)
        instance.make = validated_data.get('make', instance.make)
        instance.model_name = validated_data.get('model_name', instance.model_name)
        instance.id = validated_data.get('id', instance.id)
        instance.year = validated_data.get('year', instance.year)
        instance.save()
        return instance