from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.sign_up_page, name='signup'),
    path('', views.login_page, name='login'),
    path('logout/', views.logout_fun, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
]
