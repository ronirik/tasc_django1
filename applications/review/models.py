from django.db import models
from applications.product.models import Product
# from django.contrib.auth import get_user_model
# User = get_user_model


class Review(models.Model):
    # author = models.ForeignKey(User, on_delete=models.CASCADE,)
    product = models.ForeignKey(Product,  on_delete=models.CASCADE, related_name='review')
    descr = models.TextField(max_length=250)
    rating = models.IntegerField(choices=list(zip(range(1, 6), range(1, 6))), unique=True)
    

    def __str__(self):
        return f'{self.product} >>> {self.rating}'# >>>> {self.author}'

