from rest_framework import serializers
from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer

from categories.models import Category


__all__ = (
    'CategoriesSerializer',
    'RetrieveCategorySerializer',
)


class CategoriesSerializer(serializers.Serializer):

    name = serializers.CharField(max_length=256)
    children = serializers.ListField()

    def _process_children(self, children: list, parent: Category):
        for item in children:
            category = Category.objects.create(
                name=item['name'],
                parent=parent
            )
            if item.get('children'):
                self._process_children(item['children'], category)

    def create(self, validated_data):
        category = Category.objects.create(name=validated_data['name'])
        self._process_children(validated_data['children'], category)

        return validated_data


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name')


class RetrieveCategorySerializer(CategorySerializer):

    parents = SerializerMethodField()
    children = SerializerMethodField()
    siblings = SerializerMethodField()

    class Meta(CategorySerializer.Meta):
        fields = CategorySerializer.Meta.fields + (
            'parents',
            'children',
            'siblings',
        )

    def _get_perents(self, obj: Category):
        result = []
        while obj is not None:
            result.append(CategorySerializer(obj).data)
            obj = obj.parent

        return result

    def get_parents(self, obj: Category):
        return self._get_perents(obj.parent)

    def get_children(self, obj: Category):
        return CategorySerializer(obj.subcategories.all(), many=True).data

    def get_siblings(self, obj: Category):
        siblings = Category.objects.filter(
            parent=obj.parent
        ).exclude(
            pk=obj.id
        )
        return CategorySerializer(siblings, many=True).data
