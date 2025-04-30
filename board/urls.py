
from django.urls import path, include

from . import views
from .views import BBPosts, PostDetail, PostCreate, ResponsesCreate, PostUpdate, ResList, PrivateList, ResUpdate

urlpatterns = [
    path('', BBPosts.as_view(), name='bbposts_list'),
    path('private/', PrivateList.as_view(), name='private'),
    path('<int:pk>/', PostDetail.as_view(), name='bbposts_d'),
    path('create/', PostCreate.as_view(), name='create'),
    path('create_res/<int:pk>/', ResponsesCreate.as_view(), name='create_res'),
    path('status_res/<int:pk>/', ResUpdate.as_view(), name='status_res'),
    path('update/<int:pk>/', PostUpdate.as_view(), name='update'),
    path('responses/<int:pk>/', ResList.as_view(), name='res_list'),
]
