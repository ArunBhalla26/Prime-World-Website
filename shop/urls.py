from django.urls import path 
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_view
from .views import *
from .forms import LoginForm

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
    path("proform/", ProfileFormView.as_view(), name="proform"),
  
    path("accounts/login/", auth_view.LoginView.as_view(template_name  = "shop/LoginForm.html" ,authentication_form  = LoginForm ), name="login"),

    path("x/", xView.as_view(), name="x"),
    # path("accounts/login/", LoginFormView.as_view(), name="login_form"),
   
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
