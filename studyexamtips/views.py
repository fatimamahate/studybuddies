# from django.shortcuts import render
# from django.http import HttpResponse

# Create your views here.
# def sb_blog(request):
#     return HttpResponse("Hello World!")

from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib import messages
from django.utils.text import slugify
from .models import Post, Favorite
from .forms import CommentForm, PostForm


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

class ExamView(generic.ListView):
    """
    Filters posts so that they are published 
    and of the Exam tips category. 
    Template used is study_post_list.html
    """
    queryset = Post.objects.filter(status=1, category=2).order_by("post_created_on")
    template_name="studyexamtips/exam_post_list.html"
    paginate_by = 6

class AboutView(generic.ListView):
    """
    Filters posts so that they are published 
    and of the Exam tips category. 
    Template used is study_post_list.html
    """
    queryset = Post.objects.filter(status=1).order_by("-post_created_on")
    template_name="studyexamtips/about.html"

# class FavouriteView(generic.ListView):
#     """
#     Filters posts so that they are published 
#     and the current user has favourited it.
#     Template used is study_post_list.html
#     """
#     queryset = Post.objects.filter(status=1).order_by("post_created_on")
#     template_name="studyexamtips/my_favourites.html"
#     paginate_by = 6

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
    comments = post.comments.all().order_by("-comment_created_on")
    comment_count = post.comments.filter(approved=True).count()
    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Comment submitted and awaiting approval'
            )

    comment_form = CommentForm()

    return render(
        request,
        "studyexamtips/post_detail.html",
        {
            "post": post,
            "comments": comments,
            "comment_count": comment_count,
            "comment_form": comment_form,
        }
        
    )

# class FavoritedPostsView(generic.ListView):
#     model = Favorite
#     template_name = 'favourite_posts.html'
#     context_object_name = 'favorited_posts'

#     def get_queryset(self):
#         # Retrieve favorited posts for the logged-in user
#         return Favorite.objects.filter(user=self.request.user).select_related('post')