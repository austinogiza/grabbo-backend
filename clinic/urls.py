from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
router = DefaultRouter()

urlpatterns = [
    # path('home/', views.HomeView.as_view(), name='home'),
    path('blog-list/', views.BlogListView.as_view(), name="blog-list"),
    path('blog/<slug>/', views.BlogDetailView.as_view(), name="blog-detail"),
    path('departments/', views.DepartmentListView.as_view(), name="departments"),
    path('home-departments/', views.HomeDepartmentListView.as_view(), name="home-departments"),
    path('home-personnel/', views.HomePersonnelListView.as_view(), name="home-personnel"),
    path('departments/<slug>/', views.DepartmentListView.as_view(), name="departments-details"),
    path('personnel/', views.PersonnelListView.as_view(), name="personnel"),
    path('personnel/<slug>/', views.PersonnelDetailView.as_view(), name="personnel-details"),
    path('careers/', views.CareerListView.as_view(), name="careers"),
        path('careers/<slug>/', views.CareerDetailView.as_view(), name="careers-details"),
         path('contact/', views.ContactView.as_view(), name="contact"),
    
   
]
