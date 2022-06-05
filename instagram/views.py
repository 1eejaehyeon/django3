from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from instagram.forms import PostForm, CommentForm
from instagram.models import Post


def index(request):
    q = Post.objects.all()
    context = { "post_list": q}
    return render(request, "instagram/index.html", context)


def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect(post)
    else:
        form = PostForm()

    return render(request, "instagram/post_form.html", {
        "form": form,
    })

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comment_form = CommentForm()
    return render(request, "instagram/post_detail.html", {
        "post" : post,
        "commnet_form": comment_form,
    })


def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)  # NOTE: instance 인자(수정대상) 지정
        if form.is_valid():
            post = form.save()
            return redirect(post)
    else:
        form = PostForm(instance=post)

    return render(request, 'instagram/post_form.html', {
        'form': form,
    })