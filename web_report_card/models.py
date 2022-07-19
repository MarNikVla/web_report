from django.db import models
from django.urls import reverse


class Document(models.Model):
    docfile = models.FileField(upload_to='documents/%Y/%m/%d')

    def __str__(self):
        return self.name
    #
    # def get_absolute_url(self):
    #     return reverse('shop:product_list_by_category', args=[self.slug])
