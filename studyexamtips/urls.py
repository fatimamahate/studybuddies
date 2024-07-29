from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('study-tips/', views.StudyView.as_view(), name='study_tips'),
    path('exam-tips/', views.ExamView.as_view(), name='exam_tips'),
    path('who-we-are/', views.AboutView.as_view(), name='about'),
    # path('create/',views.CreatePost.as_view(),name='create'),
    # path('my-favorites/',views.FavoritedPostsView.as_view(), name='favorited_posts'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
   
]