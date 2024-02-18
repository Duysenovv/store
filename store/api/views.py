from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from .models import*
from .serializers import CategorySerializer, ProductSerializer, ReviewSerializer, ClientSerializer, OrderSerializer
from rest_framework import generics
from .serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated

class UserRegisterationView(generics.CreateAPIView):
    serializer_class = UserSerializer

class UserProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return super().get_object()(self)

class CategoryCreateView(CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductCreateView(CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class OrderCreateView(CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class ReviewCreateView(CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class OrderItemCreateAPIView(CreateAPIView):
    queryset = OrderItem.objects.all
    serializer_class = OrderItem    


class ClientListCreateView(generics.ListCreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class ClientDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
