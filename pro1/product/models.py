from django.db import models

# Create your models here.
class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    price = models.IntegerField()
    categoryId = models.ForeignKey(to="category.Category", on_delete=models.CASCADE)
