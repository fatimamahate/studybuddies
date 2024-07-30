from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('study-tips/', views.StudyView.as_view(), name='study_tips'),
    path('exam-tips/', views.ExamView.as_view(), name='exam_tips'),
    path('create/',views.CreatePost.as_view(),name='create'),
    path('success/', views.post_submitted,
          name='post_submit_success'),
    path('<slug:slug>/edit/',views.UpdatePost.as_view(),name='edit'),
    path('update-success/', views.post_updated,
          name='post_update_success'),
    path('who-we-are/', views.AboutView.as_view(), name='about'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
    path('<slug:slug>/edit_comment/<int:comment_id>',
         views.comment_edit, name='comment_edit'),
    path('<slug:slug>/delete_comment/<int:comment_id>',
         views.comment_delete, name='comment_delete'),
]