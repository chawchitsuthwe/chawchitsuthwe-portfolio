from django.shortcuts import render, get_object_or_404
from .models import Post, Comment, Gallery,Category
from blog.form import CommentForm

# Create your views here.
def blog(request):
    posts = Post.objects.all().order_by('-created_on')
    return render(request, 'blog.html', {'posts':posts})

def blog_detail(request, blog_id):
    blog_detail = get_object_or_404(Post, pk=blog_id)
    comments = Comment.objects.filter(post=blog_detail)
    gallerys = Gallery.objects.filter(post=blog_detail)
    form = CommentForm()
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                author=form.cleaned_data["author"],
                body=form.cleaned_data["body"],
                post=blog_detail,
            )
            comment.save()

    return render(request, 'blog_detail.html', {'post':blog_detail, 'comments':comments, 'form':form, 'gallerys':gallerys})
