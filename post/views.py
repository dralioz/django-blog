from django.shortcuts import get_object_or_404, render, HttpResponse
from .models import Post
from .forms import PostForm

# Create your views here.

# Her bir sayfanın html dosyası oluşturulacak.

def post_index(request):
    posts = Post.objects.all()
    return render(request, "post/index.html",{"posts":posts})

def post_detail(request, id):
    post = get_object_or_404(Post, id = id)
    context = {"post":post}
    return render(request, "post/detail.html",context)

def post_create(request):
    form = PostForm
    context = {"form":form}
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid:
            form.save()
    else:
        form = PostForm
    return render(request, "post/create.html",context)

def post_update(request):
    return render(request, "post/update.html",{})

def post_delete(request):
    return render(request, "post/delete.html",{})