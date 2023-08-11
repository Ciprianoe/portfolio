from django.urls import path, include
from . import views

app_name = 'blog'

urlpatterns=[
    path('',views.blog, name='blog'),
    path('<int:post_id>', views.post_details, name='postdetails'),
]