from django.shortcuts import render , redirect
from django.views.generic import TemplateView
from django.contrib import messages
from django.contrib.auth import  logout
from django.contrib.auth.forms import AuthenticationForm

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
# class ProductFilterHomePageView(TemplateView):
    
#     def get(self , request, category =None):
#         if category == None :
#             return render(request ,"shop/shop.html" , {'products'  : AllProducts(request) } )
        
#         products = Product.objects.filter(category = category)
#         return render(request ,"shop/cpage.html" , {'products'  : products  , 'category' : category} )
    

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
        

        return render(request , "shop/categoryPage.html" , {'category_names' : category_names , 'AllProducts' : AllProducts(request)})
    
    category_products  = Product.objects.filter(category = category_name_data)
    
    context = {
        'products' : products , 
        'category_name_data' : category_name_data ,
        'category_names' : category_names , 
        'category_products' : category_products,
        'AllProducts' : AllProducts(request) ,
        
        }

    return render(request , "shop/categoryPage.html" , context ) 

class ProductDetailPageView(TemplateView):
    def get(self , request ,pk ):
        product = Product.objects.get(pk = pk)
        return render(request ,"shop\ProductDetailPage.html", {"product" : product} )


# class SidebarPageView(TemplateView):
#     template_name = "shop/sidebar_list.html"


class CustomerRegistrationFormView(TemplateView):
    def get(self , request):
        form = CustomerRegistrationForm()
        return render(request , "shop/CustomerRegistrationForm.html", {"form" : form} )
    
    def post(self , request):
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            messages.success(request , " Congratulations :) Registered SucessFully ! Please Login ")
            form.save()
        
        return render(request , "shop/CustomerRegistrationForm.html", {"form" : form} )
    
class ProfileFormPageView(TemplateView):
    def get(self ,request):
        form = ProfileForm()
        return render(request , "shop/ProfilePage.html", {"form" : form} )
    
    def post(self , request):
        user = request.user
        form = ProfileForm(request.POST )
        if form.is_valid():
            print(form.errors)
            profile = form.save(commit=False)
            profile.user = request.user 
            profile.save()
            messages.success(request , " Congratulations :) Profile Added SucessFully !")
        
        return render(request , "shop/ProfilePage.html", {"form" : form} )

def LogoutView(request):
    logout(request)
    messages.success(request , " Sucessfully Loged-Out ! ")
    return redirect('login')
class AddressView(TemplateView):
    def get(self ,request):
        user  = request.user
        address_qs = Customer.objects.filter(user = user)
        return render (request , "shop/Address.html" , {'address_qs': address_qs})

    
class xView(TemplateView):
    template_name = "shop/x.html"