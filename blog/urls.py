from django.urls import path

from .views import *

urlpatterns = [
    path('<slug:category>/', PostCategory.as_view()),
    path('', PostList.as_view()),
]