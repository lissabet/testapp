from rest_framework.generics import (
    CreateAPIView,
    RetrieveAPIView,
)

from categories.models import Category
from categories.serializers import (
    CategoriesSerializer,
    RetrieveCategorySerializer,
)


class CategoriesView(CreateAPIView):

    http_method_names = ['post']
    serializer_class = CategoriesSerializer


class CategoryView(RetrieveAPIView):

    http_method_names = ['get']
    serializer_class = RetrieveCategorySerializer
    queryset = Category.objects.all()
