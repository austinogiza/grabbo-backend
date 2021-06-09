from clinic.models import Blog, Career, Contact, Departments, Professional
from clinic.serializers import BlogListSerializer, CareerListSerializer, ContactSerializer, DepartmentListSerializer, ProfessionaListSerializer
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny
# Create your views here.


class BlogListView(ListAPIView):
    serializer_class = BlogListSerializer
    queryset = Blog.objects.all().order_by('-date')
    permission_classes = (AllowAny, )


class DepartmentListView(ListAPIView):
    serializer_class = DepartmentListSerializer
    queryset = Departments.objects.all().order_by('-date')
    permission_classes = (AllowAny, )


class DepartmentDetailView(RetrieveAPIView):
    lookup_field = 'slug'
    permission_classes = (AllowAny,)
    queryset = Departments.objects.all()
    serializer_class = DepartmentListSerializer

class PersonnelListView(ListAPIView):
    serializer_class = ProfessionaListSerializer
    queryset = Professional.objects.all()
    permission_classes = (AllowAny, )

class PersonnelDetailView(RetrieveAPIView):
    lookup_field = 'slug'
    permission_classes = (AllowAny,)
    queryset = Professional.objects.all()
    serializer_class = ProfessionaListSerializer


class BlogDetailView(RetrieveAPIView):
    lookup_field = 'slug'
    permission_classes = (AllowAny,)
    queryset = Blog.objects.all()
    serializer_class = BlogListSerializer


class HomePersonnelListView(ListAPIView):
    serializer_class = ProfessionaListSerializer
    queryset = Professional.objects.all()[:6]
    permission_classes = (AllowAny, )

class HomeDepartmentListView(ListAPIView):
    serializer_class = DepartmentListSerializer
    queryset = Departments.objects.all().order_by('-date')[:4]
    permission_classes = (AllowAny, )

class CareerListView(ListAPIView):
    serializer_class = CareerListSerializer
    queryset = Career.objects.all()
    permission_classes = (AllowAny, )

class CareerDetailView(RetrieveAPIView):
    lookup_field = 'slug'
    permission_classes = (AllowAny,)
    queryset = Career.objects.all()
    serializer_class = CareerListSerializer


class ContactView(CreateAPIView):
    permission_classes = (AllowAny,)
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer