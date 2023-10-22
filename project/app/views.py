from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from app.models import Product
from app.forms import CreateProduct

# Create your views here.
class Register(SuccessMessageMixin, CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('home_page')
    template_name = 'register.html'
    success_message = 'Successfully registered!'

class ProductCreation(View):
    template_name = 'product.html'
    
    def get(self,request):
        form = CreateProduct()
        return render(request,'product.html',{'form':form})
    
    def post(self,request):
        form = CreateProduct(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            body = form.cleaned_data['body']
            new_product = Product(name=name,body=body)
            new_product.save()
            return redirect('home_page')
        else:
            return render(request,'product.html',{'form':form})