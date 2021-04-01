from django.db import models
from django.db.models import Count
from taggit.managers import TaggableManager


class Category(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = "Categories"
        ordering = ['name']

    def __str__(self):
        return self.name


class ProductQuerySet(models.query.QuerySet):
    """Personalized queryset created to improve model usability"""

    def get_counted_tags(self):
        tag_dict = {}
        query = (
            self.filter(is_public=True).annotate(tagged=Count("tags")).filter(tags__gt=0)
        )
        for obj in query:
            for tag in obj.tags.names():
                if tag not in tag_dict:
                    tag_dict[tag] = 1

                else:  # pragma: no cover
                    tag_dict[tag] += 1

        return tag_dict.items()


class Product(models.Model):
    title = models.CharField(max_length=50)
    categories = models.ManyToManyField(Category, related_name='products')
    sku = models.IntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to='images/')
    price = models.DecimalField(max_digits=8, decimal_places=2)
    qty = models.IntegerField()
    is_public = models.BooleanField(default=False)
    tags = TaggableManager()
    objects = ProductQuerySet.as_manager()

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title
    
    # use models.ManyToMany field's all() method to return all the Category objects that this product belongs to.   Ref:- 'https://www.dev2qa.com/how-to-get-many-to-many-model-field-values-in-django-view/'
    # def get_categories_values(self):
    #     ret = ''

    #     # print(self.categories.all())                  # to verify the names fetched from db

    #     for category in self.categories.all():
    #         ret = ret + category.name + ', '
    
    #     return ret
    # To use this custom function in template, you directly have to call this method's name instead of categories
