
from django.urls import path, include

from . import views
from .views import BBPosts, PostDetail, PostCreate, ResponsesCreate, PostUpdate

urlpatterns = [
    path('', BBPosts.as_view(), name='bbposts_list'),
    path('<int:pk>/', PostDetail.as_view(), name='bbposts_d'),
    path('create/', PostCreate.as_view(), name='create'),
    path('create_res/<int:pk>/', ResponsesCreate.as_view(), name='create_res'),
    path('update/<int:pk>/', PostUpdate.as_view(), name='update'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
]
