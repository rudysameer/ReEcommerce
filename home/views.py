from django.shortcuts import render
from django.views.generic import View
from .models import *
# Create your views here.
class BaseView(View):
    view = {}
    view['categories'] = Category.objects.all()
    view['brands'] = Brand.objects.all()


class HomeView(BaseView):
    def get(self,request):
        self.view
        self.view['sliders'] = Slider.objects.all()
        self.view['ads'] = Ad.objects.all()

        return render(request,'index.html',self.view)


