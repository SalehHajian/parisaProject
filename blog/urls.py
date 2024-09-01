from django.urls import path

from . import views

app_name = 'blog'

urlpatterns = [
    path('' , views.PostListView.as_view() , name ='show_post') ,
    path('<int:pk>/details/', views.PostDetailView.as_view() , name='post_detail'),
    path('create/', views.PostCreateView.as_view() , name = 'post_create') ,
    path('<int:id>/update/' , views.PostUpdateView.as_view() , name = 'post_update'),
    path('<int:id>/delete/' , views.post_delete_view , name = 'post_delete'),
]

# MVT    Model (DataBase)    View (backend)      Template (html.....)