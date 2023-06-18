from rest_framework import serializers
from productapp.models import Category,Product
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('Categoryid',
                  'CategoryName','Subcategory')

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('ProductId',
                  'Category',
                  'Name',
                  'Price',
                  )
                  