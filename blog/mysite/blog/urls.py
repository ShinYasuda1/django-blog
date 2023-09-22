from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('post_list', views.PostListView.as_view(), name='post_list'),
    path('post_create', views.PostCreateView.as_view(), name='post_create'),
    path('post_detail/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'), # 追加　(例) /blog/detail/1　※特定のレコードに対して処理を行うので pk で識別
    path('post_update/<int:pk>/', views.PostUpdateView.as_view(), name='post_update'), # 追加　(例) /blog/update/1　※同上
    path('post_delete/<int:pk>/', views.PostDeleteView.as_view(), name='post_delete'), # 追加　(例) /blog/delete/1　※同上
]
