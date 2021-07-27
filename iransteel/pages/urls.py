from django.urls import path , include
from . import views

app_name = 'pages'
urlpatterns = [
    path('',views.Pages.as_view(),name='pages'),
    path('aboutus/',views.Aboutuss.as_view(),name='aboutus'),
    path('contactus/',views.Contactus.as_view(),name='contactus'),
    path('products/',views.Products.as_view(),name='products'),
]