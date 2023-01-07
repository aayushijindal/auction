from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login_user/',views.login_user,name='login_user'),
    path('register_user/', views.register_user, name='register_user'),
    path('faq/', views.faq, name='faq'),
    path('forgot_password/', views.forgot_password, name='forgot_password'),
    path('logout/',views.logout_user, name='logout'),
    path('save_contact/', views.save_contact, name='save_contact'),
    # path('save_login/', views.save_login, name='save_login'),
    path("register_user/register", views.register, name="register")
]