from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from .permissions import IsAdminOrReadOnly
from rest_framework.views import APIView
from .models import *
from .serializers import *


class WomenViewSet(viewsets.ModelViewSet):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer 

    def get_queryset(self):
        return Women.objects.all()[:3 ]


    @action(methods=['get'], detail = False)
    def category(self, request):
        cats = Category.objects.all()
        return Response({'cats': [c.name for c in cats]})

# отдельные классы через наследование ==>
class WomenApiListPagination(PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 2


class WomenApiList(generics.ListCreateAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
    pagination_class = WomenApiListPagination
    # permission_classes = IsAuthenticatedOrReadOnly


class WomenApiUpdate(generics.RetrieveUpdateAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer 


class WomenApiDetailView(generics.RetrieveDestroyAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer 
    permission_classes = (IsAdminOrReadOnly,)


# собственные классы и методы через базовый класс APIView ==>
# class WomenApiView(APIView):
#     def get(self, request):
#         lst = Women.objects.all()
#         return Response({'posts': WomenSerializer(lst, many = True).data})


#     def post(self, request):
#         serializer = WomenSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()

        # new_post = Women.objects.create(
        #     title = request.data['title'],
        #     content = request.data['content'],
        #     cat_id = request.data['cat_id']
        # )
    #     return Response({'post': serializer.data})


    # def put(self, request, *args, **kwargs):
    #     pk = kwargs.get("pk", None)
    #     if not pk:
    #         return Response({"error":"Method put is not allowed"})

    #     try:
    #         instance = Women.objects.get(pk = pk)
    #     except:
    #         return Response({"error":"Method put is not allowed"})
    #     serializer = WomenSerializer(data = request.data, instance = instance)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response({"put": serializer.data})


    # def delete(self, request, *args, **kwargs):
    #     pk = kwargs.get("pk", None)
    #     if not pk:
    #         return Response({"error":"Method delete is not allowed"})

    #     try:
    #         instance = Women.objects.get(pk = pk)
    #     except:
    #         return Response({"error":"Method deleteeeee is not allowed"})
    #     serializer = WomenSerializer(data = request.data, instance = instance)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response({"delete": serializer.data})







