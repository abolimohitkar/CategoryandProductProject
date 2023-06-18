from django.urls import re_path
from productapp import views

urlpatterns=[
    re_path(r'^Category/$',views.CategoryApi),
    re_path(r'^Category/([0-9]+)$',views.CategoryApi),

    re_path(r'^product/$',views.productApi),
    re_path(r'^product/([0-9]+)$',views.productApi),

    
] 