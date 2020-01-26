from django.db import models


class Category(models.Model):

    name = models.CharField('Name', max_length=256)
    parent = models.ForeignKey(
        'categories.Category',
        null=True,
        related_name='subcategories',
        on_delete=models.CASCADE,
    )
