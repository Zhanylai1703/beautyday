from django.contrib import admin
from django.urls import path

from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions


from apps.discounts.views import (
    PromotionList, 
    PromotionDetail,
    CategoryList, 
    CategoryDetail, 
    SubcategoryList, 
    SubcategoryDetail, 
    ServiceList, 
    ServiceDetail
)


schema_view = get_schema_view(
    openapi.Info(
        title="Beauty Day",
        default_version="v1",
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='redoc'),
 
    path('discounts/', PromotionList.as_view(), name='promotion_list'),
    path('discounts/<int:pk>/', PromotionDetail.as_view(), name='promotion_detail'),
    path('categories/', CategoryList.as_view(), name='category_list'),
    path('categories/<int:pk>/', CategoryDetail.as_view(), name='category_detail'),
    path('subcategories/', SubcategoryList.as_view(), name='subcategory_list'),
    path('subcategories/<int:pk>/', SubcategoryDetail.as_view(), name='subcategory_detail'),
    path('services/', ServiceList.as_view(), name='service_list'),
    path('services/<int:pk>/', ServiceDetail.as_view(), name='service_detail'),
]
