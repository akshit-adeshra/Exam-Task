import datetime
from haystack import indexes
from Myshop.models import Product


class ProductIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    title = indexes.CharField(model_attr='title')

    # the field we will be using for auto completion
    content_auto = indexes.EdgeNgramField(model_attr='title')

    def get_model(self):
        return Product

    # this func is used when we are building our indexes from the cmd line, so to return as many results as many as possible
    def index_queryset(self, using=None):
        return self.get_model().objects.all()
