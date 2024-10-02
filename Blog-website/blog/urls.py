from django.urls import path
from .views import hompageview,detailview,set_rating,category_list,add_post,edit_post,search,delete_post
app_name = 'blog'
urlpatterns = [
    path('',hompageview,name='blog'),
    path('detail/<pk>/',detailview,name='detail'),
    path('rating/<value>/<pk>',set_rating,name='set_rating'),
    path('<category_slug>/posts',category_list,name='category_list'),
    path('add/',add_post,name='addpost'),
    path('edit/<int:pk>/',edit_post,name='editpost'),
    path('delete/<int:pk>/',delete_post,name='deletepost'),
    path('search/',search,name='search')
]