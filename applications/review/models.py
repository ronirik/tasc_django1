from django.db import models
from applications.product.models import Product
# from django.contrib.auth import get_user_model
# from django.contrib.auth.models import User

class Review(models.Model):
    # User = get_user_model
    # author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='review')
    product = models.ForeignKey(Product,  on_delete=models.CASCADE, related_name='review')
    descr = models.TextField(max_length=250)
    rating = models.IntegerField(choices=list(zip(range(1, 6), range(1, 6))), unique=True)
    

    def __str__(self):
        return f'{self.product} >>> {self.rating} >>>> {self.author}'

