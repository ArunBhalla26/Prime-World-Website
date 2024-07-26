from django.shortcuts import render
from django.views.generic import TemplateView
from .models  import *


# Create your views here.


class HomeView(TemplateView):
    def get (self , request):
        clothing = Product.objects.filter(category = 'Clothing')
        electronics = Product.objects.filter(category = 'Electronics')
        beauty = Product.objects.filter(category = 'Beauty & Personal Care')
        grocery = Product.objects.filter(category = 'Grocery')
        jewelry = Product.objects.filter(category = 'Jewelry')
        
        return render(request , "shop/index.html" , {'clothing' : clothing[:4] ,'electronics' : electronics[:4] , 'beauty': beauty[:4] ,'jewelry': jewelry[:4] , 'grocery': grocery[:4] }) 
    # template_name = "shop/index.html"    

class AboutView(TemplateView):
    template_name = "shop/why.html"

class ContactView(TemplateView):
    template_name = "shop/contact.html"

class TestimonialView(TemplateView):
    template_name = "shop/testimonial.html"
    
class ShopView(TemplateView):
    template_name = "shop/shop.html"

class CartegoriesView(TemplateView):
    template_name = "shop/categories.html"

