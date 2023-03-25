from rest_framework import (
    generics,
    permissions
)
from rest_framework.permissions import IsAdminUser

from .models import (
    Promotion,
    Category, 
    Subcategory, 
    Service
)

from .serializers import (
    PromotionSerializer, 
    CategorySerializer, 
    SubcategorySerializer, 
    ServiceSerializer
)


class PromotionList(generics.ListCreateAPIView):
    queryset = Promotion.objects.all()
    serializer_class = PromotionSerializer

class PromotionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Promotion.objects.all()
    permission_classes = [IsAdminUser]


class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminUser]


class SubcategoryList(generics.ListCreateAPIView):
    queryset = Subcategory.objects.all()
    serializer_class = SubcategorySerializer

class SubcategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Subcategory.objects.all()
    serializer_class = SubcategorySerializer
    permission_classes = [IsAdminUser]


class ServiceList(generics.ListCreateAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

class ServiceDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    permission_classes = [IsAdminUser]


