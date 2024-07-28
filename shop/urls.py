
from django.urls import path 
from django.conf import settings
from django.conf.urls.static import static
from .views import *


urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("about/", AboutView.as_view(), name="about"),
    path("contact/", ContactView.as_view(), name="contact"),
    path("shop/",ShopView.as_view(), name="shop"),
    path("testimonial/", TestimonialView.as_view(), name="testimonial"),
    path("cpage/",Category_Filter, name="cpage"),
    path("ppage/<int:pk>", ProductDetailPageView.as_view(), name="ppage"),
    path("side/", SidebarPageView.as_view(), name="side") ,
   path("cpage/<slug:category_name_data>", Category_Filter, name="cpage"),
   path("registration/", CustomerRegistrationFormView.as_view(), name="registration"),
    
   
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
