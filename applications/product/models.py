from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(primary_key=True)

    def __str__(self):
        return f'{self.name}'

class Product(models.Model):
    title = models.CharField(max_length=50)
    descr = models.TextField(max_length=250)
    price = models.PositiveIntegerField(default=0)  
    category = models.ForeignKey(Category,  on_delete=models.CASCADE, related_name='product')

    def __str__(self):
        return f'{self.title} >>>>  {self.descr} >>>> {self.price}'