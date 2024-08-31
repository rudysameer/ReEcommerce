from django.shortcuts import render
from django.views.generic import View
from .models import *


# Create your views here.
class BaseView(View):
    view = {}
    view['categories'] = Category.objects.all()
    view['brands'] = Brand.objects.all()


class HomeView(BaseView):
    def get(self, request):
        self.view
        self.view['sliders'] = Slider.objects.all()
        self.view['ads'] = Ad.objects.all()
        self.view['hot_products'] = Product.objects.filter(label='Hot')
        self.view['new_products'] = Product.objects.filter(label='New')
        self.view['sale_products'] = Product.objects.filter(label='Sale')
        return render(request, 'index.html', self.view)


class CategoryView(BaseView):
    def get(self, request, slug):
        # cat_id = Category.objects.get(slug = slug).id
        # self.view['cat_products'] = Product.objects.filter(category_id = cat_id)
        # self.view['category'] = Category.objects.get(slug = slug)
        category = Category.objects.get(slug=slug)
        self.view['category'] = category
        self.view['cat_products'] = Product.objects.filter(category=category)

        return render(request, 'category.html', self.view)


class BrandView(BaseView):
    def get(self, request, slug):
        brand = Brand.objects.get(slug=slug)
        self.view['bra'] = brand
        self.view['brand_products'] = Product.objects.filter(brand = brand)

        return render(request,'brand.html', self.view)
