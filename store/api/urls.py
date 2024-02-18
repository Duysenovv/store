from django.urls import path
from .views import *


name = 'api'


urlpatterns = [
    path('category/', CategoryCreateView.as_view(), name= 'category-create'),
    path('product/', ProductCreateView.as_view(), name= 'product-create'),
    path('order/', OrderCreateView.as_view(), name= 'order-create'),
    path('review/', ReviewCreateView.as_view(), name= 'review-create'),
    path('order-items/', OrderCreateView.as_view(), name= 'order-item-create'),
    path('client/', ClientListCreateView.as_view(), name='client-list-create'),
    path('clinet/', ClientDetailView.as_view(), name='client-detail')
]