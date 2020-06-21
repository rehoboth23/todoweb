"""todoweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from todo.views import (Create_User, userPage, login_user,
                        home, logout_user, Create_Todo_Front,
                        create_todo_back,
                        )

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),

    # auth
    path('signup/', Create_User.as_view(), name='signup'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),

    # todos
    path('todos/', userPage, name='userPage'),
    path('create/', Create_Todo_Front.as_view(), name='create'),
    path('addtodo/', create_todo_back, name='addtodo'),
]
