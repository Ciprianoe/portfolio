from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import Post

# Create your views here.

def blog(request):
   title= 'Blog Cipriano Escorche'
   active= 'blog'
   posts =get_list_or_404(Post)
   print(posts)  
   return render(request, 'posts/posts.html',{'posts':posts, 'title':title,'active':active })


def post_details(request, post_id):
   post=get_object_or_404(Post, pk=post_id)
   #print(post)
   return render(request,'posts/post_details.html',{'post':post})