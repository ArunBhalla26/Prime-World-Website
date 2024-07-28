from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib import messages
from .models  import *
from .forms import *

# Create your views here.

class HomeView(TemplateView):
    def get (self , request):
        clothing = Product.objects.filter(category = 'Clothing')
        electronics = Product.objects.filter(category = 'Electronics')
        beauty = Product.objects.filter(category = 'Beauty & Personal Care')
        grocery = Product.objects.filter(category = 'Grocery')
        jewelry = Product.objects.filter(category = 'Jewelry')
        
        return render(request , "shop/index.html" , {'clothing' : clothing[:4] ,'electronics' : electronics[:4] , 'beauty': beauty[:4] ,'jewelry': jewelry[:4] , 'grocery': grocery[:4] })  

class AboutView(TemplateView):
    template_name = "shop/why.html"

class ContactView(TemplateView):
    template_name = "shop/contact.html"

class TestimonialView(TemplateView):
    template_name = "shop/testimonial.html"
    
def AllProducts(request):
    return Product.objects.all()
    
class ShopView(TemplateView):
    def get(self , request):
        return render(request ,"shop/shop.html" , {'products'  : AllProducts(request) } )

def Category_Filter(request , category_name_data = None):
    # for filter section 
    products = Product.objects.all()
    category_names = []
    for category  in CATEGORY_CHOICES:
        data = category[0].split()[0].replace(',' , '')
        category_names.append(data)

    # for displaying the collections
    if ( category_name_data == None or category_name_data not in category_names):

        return render(request , "shop/categoryPage.html" , {'category_names' : category_names})
    
    category_products  = Product.objects.filter(category = category_name_data)
    
    context = {
        'products' : products , 
        'category_name_data' : category_name_data ,
        'category_names' : category_names , 'category_products' : category_products
        }

    return render(request , "shop/categoryPage.html" , context ) 

class ProductDetailPageView(TemplateView):
    def get(self , request ,pk ):
        product = Product.objects.get(pk = pk)
        return render(request ,"shop\ProductDetailPage.html", {"product" : product} )


class SidebarPageView(TemplateView):
    template_name = "shop/sidebar_list.html"


class CustomerRegistrationFormView(TemplateView):
    def get(self , request):
        form = CustomerRegistrationForm()
        return render(request , "shop/CustomerRegistrationForm.html", {"form" : form} )
    
    def post(self , request):
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            messages.success(request , " Congratulations :) Registered SucessFully !")
            form.save()
        
        return render(request , "shop/CustomerRegistrationForm.html", {"form" : form} )


