from unittest import TestCase
from unittest.mock import MagicMock, patch


from categories.serializers import CategoriesSerializer


class CategoriesSerializerProcessChildrenTests(TestCase):

    @patch('categories.serializers.Category.objects')
    def test_ok(self, objects_mock):
        parent_mock = MagicMock()
        create_mock = MagicMock(return_value=parent_mock)
        objects_mock.create = create_mock
        children_mock = [
            {
                "name": "Category 1.1",
                "children": [
                    {
                        "name": "Category 1.1.1",
                        "children": [
                            {"name": "Category 1.1.1.1"},
                            {"name": "Category 1.1.1.2"},
                            {"name": "Category 1.1.1.3"}
                        ]
                    },
                    {
                        "name": "Category 1.1.2",
                        "children": [
                            {"name": "Category 1.1.2.1"},
                            {"name": "Category 1.1.2.2"},
                            {"name": "Category 1.1.2.3"}
                        ]
                    }
                ]
            },
            {
                "name": "Category 1.2",
                "children": [
                    {"name": "Category 1.2.1"},
                    {
                        "name": "Category 1.2.2",
                        "children": [
                            {"name": "Category 1.2.2.1"},
                            {"name": "Category 1.2.2.2"}
                        ]
                    }
                ]
            }
        ]

        CategoriesSerializer()._process_children(children_mock, parent_mock)
        self.assertEqual(create_mock.call_count, 14)
