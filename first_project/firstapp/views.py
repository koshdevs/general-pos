from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import ListView,CreateView,UpdateView,DetailView
from django.contrib.messages.views import SuccessMessageMixin
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from django.views.decorators.csrf import csrf_protect,csrf_exempt
from django.utils.decorators import method_decorator
from .models import Stocks,Shops
# Create your views here.
orders = [
    {
        'title':"today orders",
        'qty':10
    },
    
]
def home(request):
    data={
        "orders":orders
    }
    return render(request,'firstapp/home.html',data)

def counter(request):
  
    stocks = {
        'products': Stocks.objects.all()
    }
    return render(request,'firstapp/counter.html',stocks)

def getCounter(request):
    name  = request.GET.get("p_name")
    qty = request.GET.get("qty")
    price = request.GET.get("price")
    total = float(price)*int(qty)
    data = {"name":name,"qty":qty,"price":price,"total":total}
    print(data)
    return JsonResponse(data,status=200)

def stocksView(request):
    if request.POST:
        date1 = request.POST.get("date1")
        date2 = request.POST.get("date2")
        if date1!='' or date1!='':
            products = Stocks.objects.filter(p_created__range=[date1,date2])
        else: 
            products = Stocks.objects.all()
    products = Stocks.objects.all()  
    page_num = request.GET.get('page',1)
    paginator = Paginator(products,5)
    try:
        page_obj = paginator.page(page_num)
    except PageNotAnInteger: 
        page_obj =paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)
        
    contxt = {
        'products':products,
        'page_obj': page_obj
    }
    
    return render(request,'firstapp/stocks.html',contxt)

class StocksCreateView(CreateView):
    model = Stocks
    template_name = 'firstapp/add_stocks.html'
    fields = ['p_name','p_category','p_desc',
              'p_image','p_qty','p_price','p_cost','p_created'
              ]
    
    def form_valid(self,form):
        form.instance.p_creator = self.request.user
        return super().form_valid(form)
    
class StocksDetailView(DetailView):
    model= Stocks

class StocksUpdateView(UpdateView):
    model = Stocks
    template_name = 'firstapp/update_stocks.html'
    fields = ['p_name','p_category','p_desc',
              'p_image','p_qty','p_price','p_cost','p_created'
              ]
    
    def form_valid(self,form):
        form.instance.p_creator = self.request.user
        return super().form_valid(form)
    
    


class ShopsCreateView(SuccessMessageMixin,CreateView):
    model = Shops
    template_name = 'firstapp/add_shops.html'
    success_message = ' shop added successfully'
    fields =['shop_name','shop_cat','shop_loc','shop_auth']
    
    def form_valid(self,form):
        return super().form_valid(form)