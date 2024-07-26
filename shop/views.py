from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.


class HomeView(TemplateView):
    template_name = "shop/index.html"    


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

# class AboutView(TemplateView):
#     template_name = "why.html"