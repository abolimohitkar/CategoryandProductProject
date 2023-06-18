from django.shortcuts import render
from productapp.models import Category,Product
from productapp.serializer import CategorySerializer,ProductSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

@csrf_exempt
def CategoryApi(request,id=0):
    if request.method=='GET':
        Categories = Category.objects.all()
        Categories_serializer = CategorySerializer(Categories, many=True)
        return JsonResponse(Categories_serializer.data, safe=False)

    elif request.method=='POST':
        category_data=JSONParser().parse(request)
        Categories_serializer = CategorySerializer(data=category_data)
        if Categories_serializer.is_valid():
            Categories_serializer.save()
            return JsonResponse("Category Added Sucessfully!!" , safe=False)
        return JsonResponse("Failed to Add Category.",safe=False)
    
    elif request.method=='PUT':
        category_data = JSONParser().parse(request)
        category=Category.objects.get(Categoryid=category_data['Categoryid'])
        Categories_serializer=CategorySerializer(category,data=category_data)
        if Categories_serializer.is_valid():
            Categories_serializer.save()
            return JsonResponse("Category Updated Sucessfully!!", safe=False)
        return JsonResponse("Failed to Update Category.", safe=False)

    elif request.method=='DELETE':
        category=Category.objects.get(Categoryid=id)
        category.delete()
        return JsonResponse("Deleted Sucessfully!!", safe=False)

@csrf_exempt
def productApi(request,id=0):
    if request.method=='GET':
        product = Product.objects.all()
        product_serializer = ProductSerializer(product, many=True)
        return JsonResponse(product_serializer.data, safe=False)

    elif request.method=='POST':
        product_data=JSONParser().parse(request)
        product_serializer = ProductSerializer(data=product_data)
        if product_serializer.is_valid():
            product_serializer.save()
            return JsonResponse("Added Sucessfully!!" , safe=False)
        return JsonResponse("Failed to Add.",safe=False)
    
    elif request.method=='PUT':
        product_data = JSONParser().parse(request)
        product=Product.objects.get(ProductId=product_data['ProductId'])
        product_serializer=ProductSerializer(product,data=product_data)
        if product_serializer.is_valid():
            product_serializer.save()
            return JsonResponse("Updated Sucessfully!!", safe=False)
        return JsonResponse("Failed to Update.", safe=False)

    elif request.method=='DELETE':
        product=Product.objects.get(ProductId=id)
        product.delete()
        return JsonResponse("Deleted Sucessfully!!", safe=False)
