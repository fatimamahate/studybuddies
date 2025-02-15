from .models import Post, Comment
from django import forms
from django_summernote.widgets import SummernoteWidget

# Set up forms with fields and widgets needed for the form
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','main_body','featured_image','preview','difficulty','category', 'status')
        widgets = {
            'main_body': SummernoteWidget(),
        }