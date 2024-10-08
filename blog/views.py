from django.shortcuts import render , get_object_or_404 , redirect
from django.views import generic
from .models import Post
from .forms import NewPostForm
from django.urls import reverse_lazy
# Create your views here.



class PostListView(generic.ListView) :
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'

    def get_queryset(self) :
        return Post.objects.filter(status = 'pub').order_by('-update_date')



class PostDetailView(generic.DetailView):
    model = Post
    template_name = 'blog/post_details.html'
    context_object_name = 'post'


class PostCreateView(generic.CreateView) :
    form_class = NewPostForm
    template_name = 'blog/post_create.html'



class PostUpdateView(generic.UpdateView) :
    model = Post
    form_class = NewPostForm
    template_name = 'blog/post_create.html'



class PostDeleteView(generic.DetailView) :
    model = Post
    template_name = 'blog/post_delete.html'
    success_url = reverse_lazy('blog:post_list')




