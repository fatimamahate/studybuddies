# from django.shortcuts import render
# from django.http import HttpResponse

# Create your views here.
# def sb_blog(request):
#     return HttpResponse("Hello World!")

from django.shortcuts import render
from django.views import generic
from .models import Post

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by("post_created_on")
    # template_name = "post_list.html"
    template_name = "studyexamtips/index.html"
    paginate_by = 4
