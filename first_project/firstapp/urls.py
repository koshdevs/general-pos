from django.urls import path
from . import views
from .views import StocksCreateView,ShopsCreateView,StocksUpdateView
urlpatterns = [
    path('', views.home,name='firstapp-home'),
    path('counter/', views.counter,name='firstapp-counter'),
    path('getcounter', views.getCounter,name='firstapp-getcounter'),
    path('stocks/list',views.stocksView,name="firstapp-stocks"),
    path('stocks/addstocks/',StocksCreateView.as_view(),name="firstapp-addstocks"),
    path('stocks/<int:pk>/updates',StocksUpdateView.as_view(),name="firstapp-updatestocks"),
    path('addshops/',ShopsCreateView.as_view(),name="firstapp-addshops")
]