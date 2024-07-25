from django.db import models
from django.contrib.auth.models import User
# Create your models here.

STATUS = ((0, "Draft"), (1, "Published"))
DIFFICULTY_LEVELS = ((0, "All Levels"),(1, "Beginner"), (2, "Intermediate"), (3, "Advanced"))
CATEGORY = ((0, "No Category"), (1, "Study Tips"), (2, "Exam Tips"))

class Post(models.Model):
    title = models.CharField(max_length=250, unique=True)
    subject = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="studyexam_posts")
    main_body = models.TextField()
    preview = models.TextField(blank=True)
    post_created_on = models.DateTimeField(auto_now_add=True)
    post_updated_on = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)
    difficulty = models.IntegerField(choices=DIFFICULTY_LEVELS, default=0)
    approved = models.BooleanField(default=False)


