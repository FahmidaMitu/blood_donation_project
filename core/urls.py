from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    
    path('donors/', views.donor_list, name='donor_list'),
    path('donor/<int:pk>/', views.donor_detail, name='donor_detail'),
    path('donor/profile/', views.create_or_edit_donor_profile, name='donor_profile'),
    
    path('requests/', views.request_list, name='request_list'),
    path('request/new/', views.create_request, name='create_request'),
    path('request/<int:pk>/', views.request_detail, name='request_detail'),
    path('request/<int:pk>/edit/', views.edit_request, name='edit_request'),
    path('request/<int:pk>/delete/', views.delete_request, name='delete_request'),
    path('my-requests/', views.my_requests, name='my_requests'),
]