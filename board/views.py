from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse_lazy

from .forms import LoginForm, RegisterForm, PostForm, ResponsesForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from .models import Posts, Responses


# Create your views here.

class BBPosts(ListView):
    model = Posts
    template_name = 'flatpages/board_list.html'
    context_object_name = 'posts'


class PostCreate(PermissionRequiredMixin, CreateView):
    form_class = PostForm
    model = Posts
    template_name = 'flatpages/add.html'
    permission_required = ()
    success_url = reverse_lazy('bbposts_list')

    def form_valid(self, form):
        post = form.save(commit=False)
        post.user = User.objects.get(id=self.request.user.pk)
        post.save()
        return super().form_valid(form)


class ResponsesCreate(PermissionRequiredMixin, CreateView):
    form_class = ResponsesForm
    model = Responses
    template_name = 'flatpages/add.html'
    permission_required = ()
    success_url = reverse_lazy('bbposts_list')

    def form_valid(self, form):
        res = form.save(commit=False)
        res.user = User.objects.get(id=self.request.user.pk)
        res.post = Posts.objects.get(id=self.request.path[-2])
        res.status = 'CN'
        res.save()
        return super().form_valid(form)


class PostUpdate(PermissionRequiredMixin, LoginRequiredMixin, UpdateView):
    form_class = PostForm
    model = Posts
    template_name = 'flatpages/add.html'
    permission_required = ()
    success_url = reverse_lazy('bbposts_list')


class PostDetail(DetailView):
    model = Posts
    template_name = 'flatpages/board_detail.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post_id = self.request.path[-2]
        context['responses'] = Responses.objects.filter(post=post_id)


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('bbposts_list')
    else:
        form = LoginForm()
    return render(request, 'flatpages/login.html', {'form': form})


def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'flatpages/register.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('login')
