from django.db import models

class Category(models.Model):
    Categoryid = models.AutoField(primary_key=True)
    CategoryName = models.CharField(max_length=100)
    Subcategory=models.CharField(max_length=100)
    def __str__(self):
        return "{}.{}.{}.format(self.Categoryid,self.CategoryName,self.Subcategory)"

class Product(models.Model):
    ProductId = models.AutoField(primary_key=True)
    Category = models.CharField(max_length=100)
    Name = models.CharField(max_length=100)
    Price = models.BigIntegerField(

    )

    def __str__(self):
        return "{}.{}.{}.format(self.productId,self.Category,self.Name,self.Price)"