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
                        logout_user,create_todo_back, return_view,
                        complete_item, delete_item, search_view
                        )

urlpatterns = [
    path('admin/', admin.site.urls),

    # auth
    path('signup/', Create_User.as_view(), name='signup'),
    path('', login_user, name='login'),
    path('logout/', logout_user, name='logout'),

    # todos
    path('dashboard/', userPage, name='dashboard'),
    path('spec/<str:spec>', userPage, name='spec'),
    path('addtodo/', create_todo_back, name='addtodo'),

    # others
    path('return/', return_view, name='return'),
    path('complete/<int:id>', complete_item, name='complete'),
    path('delete/<int:id>', delete_item, name='delete'),
    path('search', search_view, name='search'),
]
