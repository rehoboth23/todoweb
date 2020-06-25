from django.urls import path
from .views import (Create_User, userPage, login_user,
                        logout_user,create_todo_back, complete_item,
                        delete_item, search_view, return_to_prev
                        )
app_name = 'todo'
urlpatterns = [
    # auth
    path('', login_user, name='login'),
    path('signup/', Create_User.as_view(), name='signup'),
    path('logout/', logout_user, name='logout'),

    # todos
    path('dashboard/', userPage, name='dashboard'),
    path('spec/<str:spec>', userPage, name='spec'),
    path('addtodo/', create_todo_back, name='addtodo'),

    # others
    path('complete/<int:id>', complete_item, name='complete'),
    path('delete/<int:id>', delete_item, name='delete'),
    path('search', search_view, name='search'),
    path('prev', return_to_prev, name='prev'),
]
