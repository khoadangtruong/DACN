from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from home.models import Setting
from product.models import Product, Category, Images
from home.form import SearchForm

def index(request):
    setting = Setting.objects.get(pk = 1)
    category = Category.objects.all()
    products_top10 = Product.objects.all().order_by('id')[:9]
    products_new = Product.objects.all().order_by('-id')[:9]
    page = 'home'
    context = {
        'setting': setting, 
        'page': page,
        'category': category,
        'products_top10': products_top10,
        'products_new': products_new,
    }
    return render(request, 'index.html', context)

def about(request):
    setting = Setting.objects.get(pk = 1)
    context = {
        'setting': setting,
    }
    return render(request, 'about.html', context)

def contact(request):
    setting = Setting.objects.get(pk = 1)
    context = {
        'setting': setting,
        }
    return render(request, 'contact.html', context)

def category_products(request, id, slug):
    setting = Setting.objects.get(pk = 1)
    products = Product.objects.filter(category_id = id)
    category = Category.objects.all()
    context = {
        'products': products,
        'category': category,
        'setting': setting,
    }
    return render(request, 'category_products.html', context)

def shop(request):
    all_products = Product.objects.all()
    category = Category.objects.all()
    context = {
        'all_products': all_products,
        'category': category,
    }
    return render(request, 'shop.html', context)

def search(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data['query']
            catid = form.cleaned_data['catid']
            if catid == 0:
                products = Product.objects.filter(title__icontains=query)
            else:
                products = Product.objects.filter(title__icontains=query, category_id=catid)
            
            category = Category.objects.all()
            context = {
                'products': products,
                'query': query,
                'category': category,
            }
            return render(request, 'search_products.html', context)
    
    return HttpResponseRedirect('/')

def product_detail(request, id, slug):
    category = Category.objects.all()
    product = Product.objects.get(pk = id)
    images = Images.objects.filter(product_id=id)
    context = {
        'product': product,
        'category': category,
        'images': images
    }
    return render(request, 'product_detail.html', context)

