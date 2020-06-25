from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from .forms import Signup_Form, Create_Todo_Form, Signin_Form
from .models import Todo
from django.contrib.auth import login, authenticate, logout
from datetime import date


# Create your views here.
def complete_item(request, id):
    obj = get_object_or_404(Todo, id=id, user=request.user)
    obj.complete()
    obj.save()
    return redirect('todo:dashboard')


def return_to_prev(request):
    return redirect('../../')


def search_view(request):
    user = request.user
    string = str(request.GET.get('todo:search'))
    if user and user.is_authenticated:
        querylist = [object for object in Todo.objects.all() if object.search(string)]
        context = {
            'todos': querylist,
            'title': string
        }
        return render(request, 'userpage.html', context)


def delete_item(request, id):
    obj = get_object_or_404(Todo, id=id, user=request.user)
    obj.delete()
    return redirect('../spec/completed')


def login_user(request):
    user = request.user
    if user and user.is_authenticated:
        return redirect('todo:dashboard')
    else:
        if request.method == 'GET':
            context = {
                'form': Signin_Form
            }
            return render(request, 'index.html', context)

        else:
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('../dashboard/')
            else:
                return redirect('todo:login')


def logout_user(request):
    if request.method == 'POST':
        logout(request)
        return redirect('todo:login')


def userPage(request, spec=None):
    user = request.user
    if user and user.is_authenticated:
        if spec is None:
            if user and user.is_authenticated:
                querylist = Todo.objects.filter(user=user, completed=False)
                context = {
                    'todos': querylist,
                    'title': 'All'
                }
                return render(request, 'userpage.html', context)

            else:
                return redirect('todo:login')
        else:
            if spec == 'important':
                important = Todo.objects.filter(important=True, completed=False, user=user)
                return render(request, 'userpage.html', {'title': 'IMPORTANT', 'spec':True, 'todos':important})
            elif spec == 'urgent':
                urgent = Todo.objects.filter(urgent=True, completed=False, user=user)
                return render(request, 'userpage.html', {'title': 'URGENT', 'spec':True, 'todos':urgent})
            elif spec == 'due_soon':
                due_soon = [obj for obj in Todo.objects.all() if obj.due_soon() and obj.completed==False and obj.user==user]
                return render(request, 'userpage.html', {'title': 'DUE SOON', 'spec':True, 'todos':due_soon})
            elif spec == 'completed':
                querylist = Todo.objects.filter(user=user, completed=True)

                return render(request, 'userpage.html', {'title': 'COMPLETE', 'spec':True, 'todos':querylist})
            elif spec == 'create':
                querylist = Todo.objects.filter(user=user)
                form = Create_Todo_Form
                return render(request, 'userpage.html', {'title': 'CREATE', 'spec':True, 'todos':querylist, 'form': form})


def create_todo_back(request):
    if request.method == 'POST':
        form = Create_Todo_Form(request.POST)
        if form.is_valid():
            newtodo = form.save(commit=False)
            newtodo.user = request.user
            newtodo.save()
            return redirect('todo:dashboard')
        else:
            user = request.user
            querylist = Todo.objects.filter(user=user)
            form = Create_Todo_Form
            return render(request, 'userpage.html', {'title': 'CREATE', 'spec': True, 'todos': querylist, 'form': form})


class Create_User(generic.CreateView):
    template_name = 'signup.html'
    form_class = Signup_Form
    user = None

    def form_valid(self, form):
        self.user = form.save()

        return super().form_valid(form)

    def get_success_url(self):
        login(self.request, self.user)
        return '../dashboard'
