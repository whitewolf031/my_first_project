from rest_framework import serializers
from .models import Person

# class PersonModelSerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     first_name = serializers.CharField(max_length=25)
#     last_name = serializers.CharField(max_length=25)
#     about = serializers.CharField(max_length=255)
#     admin_or_not = serializers.BooleanField(default=False)
#     created_at = serializers.DateTimeField(read_only=True)
#
#     def create(self, validated_data):
#         return Person.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         instance.first_name = validated_data.get("first_name", instance.first_name)
#         instance.last_name = validated_data.get("last_name", instance.last_name)
#         instance.about = validated_data.get("about", instance.about)
#         instance.admin_or_not = validated_data.get("admin_or_not", instance.admin_or_not)
#         instance.save()
#         return instance

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = "__all__"
        # fields = ["first_name", "last_name", "about", "admin_or_not"]