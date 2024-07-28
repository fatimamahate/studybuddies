# from django.shortcuts import render
# from django.http import HttpResponse

# Create your views here.
# def sb_blog(request):
#     return HttpResponse("Hello World!")

from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Post

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by("post_created_on")
    template_name = "studyexamtips/index.html"
    paginate_by = 6

class StudyView(generic.ListView):
    """
    Filters posts so that they are published 
    and of the study tips category. 
    Template used is study_post_list.html
    """
    queryset = Post.objects.filter(status=1, category=1).order_by("post_created_on")
    template_name="studyexamtips/study_post_list.html"
    paginate_by = 6



def post_detail(request, slug):
    """
    Display an individual :model:`blog.Post`.

    **Context**

    ``post``
        An instance of :model:`blog.Post`.

    **Template:**

    :template:`blog/post_detail.html`
    """

    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)

    return render(
        request,
        "studyexamtips/post_detail.html",
        {"post": post},
    )