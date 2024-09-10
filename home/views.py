from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render,get_object_or_404,redirect
from django.views.generic import View
from .models import *
from django.db.models import Q


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
        self.view['brand'] = brand
        self.view['brand_products'] = Product.objects.filter(brand=brand)

        return render(request, 'brand.html', self.view)


class ProductDetailView(BaseView):
    def get(self, request, slug):

        # self.view['product_details'] = Product.objects.filter(slug=slug)
        # product_detail = Product.objects.get(slug=slug)
        product_detail = get_object_or_404(Product, slug=slug)
        self.view['product_details'] = product_detail
        related_brands = product_detail.brand
        self.view['related_brands'] = Product.objects.filter(brand = related_brands).exclude(slug = slug)
        related_label = product_detail.label
        self.view['related_label'] = Product.objects.filter(label = related_label).exclude(slug = slug)


        return render(request,'product-detail.html',self.view)


class SearchView(BaseView):
    def get(self,request):
        self.view
        # if request.method == 'POST':
        #     query = request.GET('search')
        query = request.GET.get('search')
        if query != '':
            self.view['search_products'] = Product.objects.filter(
                Q(product_name__icontains = query)| Q(description__icontains = query)
            )

        elif query == ' ':
            return redirect('/')

        else:
            return redirect('/')



        return render(request,'search.html',self.view)


def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        first_name = request.POST['fname']
        last_name = request.POST['lname']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']

        if password == cpassword:
            if User.objects.filter(username = username).exists():
                messages.error(request,"Username already exists. try new")
                return redirect("/signup")
            elif User.objects.filter(email = email).exists():
                messages.error(request,"Email is already occupied. try new")

            else:
                User.objects.create_user(
                    username = username,
                    email = email,
                    first_name = first_name,
                    last_name = last_name,
                    password=password
                )
                messages.success(request,"User successfully created")
                return redirect("/")

        else:
            messages.error(request,"Passwords donot match")
            return redirect("/signup")

    return render(request,'signup.html')


class CartView(BaseView):
    def get(self,request):
        username = request.user.username

        self.view['cart_products'] = Cart.objects.filter(name = username, checkout = False)



        return render(request,'cart.html',self.view)


