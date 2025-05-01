from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator

from .filters import ResponsesFilter
from .forms import RegisterForm, PostForm, ResponsesForm, ResponsesStatusForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from .models import Posts, Responses


# Create your views here.

class BBPosts(ListView):
    model = Posts
    template_name = 'flatpages/board_list.html'
    context_object_name = 'posts'


@method_decorator(login_required, name='dispatch')
class PostCreate(LoginRequiredMixin, CreateView):
    form_class = PostForm
    model = Posts
    template_name = 'flatpages/add.html'

    success_url = reverse_lazy('bbposts_list')

    def form_valid(self, form):
        post = form.save(commit=False)
        post.user = User.objects.get(id=self.request.user.pk)
        post.save()
        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
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


@method_decorator(login_required, name='dispatch')
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


class ResList(ListView):
    model = Responses
    template_name = 'flatpages/res_list.html'
    context_object_name = 'responses'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['res_list'] = Responses.objects.filter(post=Posts.objects.get(id=self.request.path[-2]))
        return context


@method_decorator(login_required, name='dispatch')
class PrivateList(ListView):
    model = Responses
    template_name = 'flatpages/private.html'
    context_object_name = 'res'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = User.objects.get(id=self.request.user.pk)
        context['user'] = user
        post_list = Posts.objects.filter(user=user)
        context['post_list'] = post_list
        res_list = []
        for post in post_list:
            res_list.append(post.responses.all())
        context['res_list'] = res_list
        context['filterset'] = self.filterset
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = ResponsesFilter(self.request.GET, queryset)
        return self.filterset.qs


@method_decorator(login_required, name='dispatch')
class ResUpdate(PermissionRequiredMixin, LoginRequiredMixin, UpdateView):
    form_class = ResponsesStatusForm
    model = Posts
    template_name = 'flatpages/add.html'
    permission_required = ()
    success_url = reverse_lazy('private')
