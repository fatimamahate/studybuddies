from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('study-tips/', views.StudyView.as_view(), name='study_tips'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
    
]