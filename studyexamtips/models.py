from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
# Create your models here.

STATUS = ((0, "Draft"), (1, "Published"))
DIFFICULTY_LEVELS = ((0, "All Levels"),(1, "Beginner"), (2, "Intermediate"), (3, "Advanced"))
CATEGORY = ((0, "Uncategorised"), (1, "Study"), (2, "Exam"))

class Post(models.Model):
    title = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="studyexam_posts")
    featured_image = CloudinaryField('image', default='placeholder')
    main_body = models.TextField()
    preview = models.TextField(blank=True)
    post_created_on = models.DateTimeField(auto_now_add=True)
    post_updated_on = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)
    difficulty = models.IntegerField(choices=DIFFICULTY_LEVELS, default=0)
    approved = models.BooleanField(default=False)
    category = models.IntegerField(choices=CATEGORY, default=0)

    class Meta:
        ordering = ["-post_created_on"]
    
    def __str__(self):
        return f"{self.title} by {self.author}."
    



class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comment_author")
    nickname = models.CharField(max_length=30)
    body = models.TextField()
    comment_created_on = models.DateTimeField(auto_now_add=True)
    comment_updated_on = models.DateTimeField(auto_now=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["-comment_created_on"]
    
    def __str__(self):
        return f"{self.author} commented on {self.post}"






