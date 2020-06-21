from django.shortcuts import render, redirect
from django.views import generic
from .forms import Signup_Form, Create_Todo_Form, UserCreationForm
from .models import Todo
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm


# Create your views here.
def login_user(request):
    if request.method == 'GET':
        context = {
            'form': AuthenticationForm
        }
        return render(request, 'signin.html', context)

    else:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('../todos/')
        else:
            print(user)
            return redirect('home')


def logout_user(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')


def userPage(request):
    user = request.user

    if user and user.is_authenticated:
        querylist = Todo.objects.filter(user=user)
        context = {
            'todos': querylist
        }
        return render(request, 'userPage.html', context)

    else:
        return redirect('login')


def create_todo_back(request):
    if request.method == 'POST':
        print('here')
        form = Create_Todo_Form(request.POST)
        if form.is_valid():
            newtodo = form.save(commit=False)
            newtodo.user = request.user
            newtodo.save()
            return redirect('userPage')


def home(request):
    user = request.user
    if user.is_authenticated:
        return redirect('userPage')

    else:
        context = {

        }
        return render(request, 'home.html', context)


class Create_User(generic.CreateView):
    template_name = 'signup.html'
    form_class = Signup_Form

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return '../login/'


class Create_Todo_Front(generic.CreateView):
    template_name = 'create.html'
    form_class = Create_Todo_Form
