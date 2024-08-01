# from django.shortcuts import render
# from django.http import HttpResponse

# Create your views here.
# def sb_blog(request):
#     return HttpResponse("Hello World!")

from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.utils.text import slugify
from .models import Post, Comment
from .forms import CommentForm, PostForm


class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by("-status", "-post_updated_on")
    template_name = "studyexamtips/index.html"
    paginate_by = 6

class StudyView(generic.ListView):
    """
    Filters posts so that they are published 
    and of the study tips category. 
    Template used is study_post_list.html
    """
    queryset = Post.objects.filter(status=1, category=1).order_by("-post_created_on")
    template_name="studyexamtips/study_post_list.html"
    paginate_by = 6

class ExamView(generic.ListView):
    """
    Filters posts so that they are published 
    and of the Exam tips category. 
    Template used is study_post_list.html
    """
    queryset = Post.objects.filter(status=1, category=2).order_by("-post_created_on")
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

class MyPostsView(generic.ListView):
    template_name = "studyexamtips/my_posts_list.html"
    paginate_by = 6
    def get_queryset(self):

        return Post.objects.filter(author=self.request.user.id).order_by(
                                   '-post_created_on')
# try adding this to a class based listview
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

def comment_edit(request, slug, comment_id):
    """
    view to edit comments
    """
    if request.method == "POST":

        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.author == request.user:
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.approved = False
            comment.save()
            messages.add_message(request, messages.SUCCESS, 'Comment Updated Successfully')
        else:
            messages.add_message(request, messages.ERROR, 'Error: the comment was not updated')

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))

def comment_delete(request, slug, comment_id):
    """
    view to delete comment
    """
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, 'Comment Deleted Successfully')
    else:
        messages.add_message(request, messages.ERROR, 'Only comments you have posted can be deleted')

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))


class CreatePost(generic.CreateView):
    model = Post
    form_class = PostForm
    template_name = 'studyexamtips/create_post.html'
    success_url = '/success'

    def form_valid(self, form):
       
        form.instance.author = self.request.user
        form.instance.slug = slugify(form.instance.title)
        return super().form_valid(form)

def post_submitted(request):

    return render(request, 'studyexamtips/post_submitted.html')

class UpdatePost(generic.UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'studyexamtips/update_post.html'
    success_url = '/update-success'

    def form_valid(self, form):
       
        form.instance.author = self.request.user
        form.instance.slug = slugify(form.instance.title)

        return super().form_valid(form)

def post_updated(request):

    return render(request, 'studyexamtips/post_updated.html')

class DeletePost(generic.DeleteView):

    model = Post
    template_name = 'studyexamtips/delete_post.html'
    success_url = '/delete-success'

def post_deleted(request):

    return render(request, 'studyexamtips/post_deleted.html')


def search_post(request):
    """ search function  """
    if request.method == "POST":
        query_name = request.POST.get('title', None)
        if query_name:
            results = Post.objects.filter(title__contains=query_name)
            return render(request, 'studyexamtips/post_search.html', {"results":results})

    return render(request, 'studyexamtips/post_search.html')

# def search_post(request):
#     if request.method == 'POST':
#         # Retrieve the search query entered by the user
#         search_query = request.POST['search_query']
#         # Filter your model by the search query
#         posts = Post.objects.filter(title__contains=search_query)
#         return render(request, 'studyexamtips/post_search.html', {'query':search_query, 'posts':posts})
#     else:
#         return render(request, 'studyexamtips/post_search.html',{})

def my_404(request, exception):
    context = {}
    return render(request, 'studyexamtips/404.html',context)


