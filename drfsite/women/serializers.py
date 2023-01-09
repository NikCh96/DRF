from rest_framework import serializers
import io
from .models import *
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser


class WomenSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default = serializers.CurrentUserDefault)

    class Meta:
        model = Women
        fields = ('title', 'content', 'time_create','cat','user')


# class WomenSerializer(serializers.Serializer):
#     title = serializers.CharField(max_length = 255,read_only = True)
#     content = serializers.CharField(read_only = True)
#     time_create = serializers.DateTimeField(read_only = True)
#     is_published = serializers.BooleanField(default=True)
#     cat_id = serializers.IntegerField(read_only = True)

#     def create(self, validated_data):
#         return Women.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         instance.title = validated_data.get("title", instance.title)
#         instance.content = validated_data.get("content", instance.content)
#         instance.is_published = validated_data.get("is_published", instance.is_published)
#         instance.cat_id = validated_data.get("cat_id", instance.cat_id)
#         instance.save()
#         return instance

#     def delete(self, validated_data):
#         return Women.objects.delete(**validated_data)


# class WomenModel:
#     def __init__ (self, title, content):
#         self.title = title
#         self.content = content
        

# class WomenSerializer(serializers.Serializer):
#    title = serializers.CharField(max_length = 255)
#    content  = serializers.CharField()


# def encode():
#     model  = WomenModel('Angelina Joli','Bradd Pitt')
#     model_sr = WomenSerializer(model)
#     print(model_sr.data, type(model_sr.data), sep = '\n')
#     json = JSONRenderer().render(model_sr.data)
#     print(json)


# def decode():
#     stream = io.BytesIO(b'{"title":"Angelina Joli","content":"Bradd Pitt"}')
#     data = JSONParser().parse(stream)
#     serializer = WomenSerializer(data = data)
#     serializer.is_valid()
#     print(serializer.validated_data)