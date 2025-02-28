from django.urls import path
from Login_app import views



app_name = 'Login_app'
urlpatterns = [
    path('', views.index, name="index"),
    path('register/', views.register, name="register"),
    path('login/', views.logIn, name="login"),
    path('user_login/', views.user_login, name="user_login"),
    path('user_logout/', views.logOut, name="logout")

]
