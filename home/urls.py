from django.urls import path
from .views import *

urlpatterns = [
    path("", HomeView.as_view(), name='home'),
    path("category/<slug>", CategoryView.as_view(), name='category'),
    path("brand/<slug>", BrandView.as_view(), name='brand'),
    path("product/<slug>", ProductDetailView.as_view(), name='productDetail'),
    path("search", SearchView.as_view(), name="search"),
    path("signup", signup, name="signup"),
]
