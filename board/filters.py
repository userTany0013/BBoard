import django_filters
from django.forms import DateInput
from django_filters import FilterSet, ModelMultipleChoiceFilter

from .models import Posts


class ResponsesFilter(FilterSet):
    post = ModelMultipleChoiceFilter(
        field_name='post',
        queryset=Posts.objects.all(),
        label='Посты',
    )
