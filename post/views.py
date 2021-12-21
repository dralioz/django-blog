from django.http.response import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render, HttpResponse
from .models import Post
from .forms import PostForm
from django.contrib import messages

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
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save()
            return HttpResponseRedirect(post.get_absolute_url())
    else:
        form = PostForm
    
    context = {"form":form}
    return render(request, "post/create.html",context)

def post_update(request, id):
    post = get_object_or_404(Post,id=id)
    form = PostForm(request.POST or None, instance=post)
    if form.is_valid():
        form.save()
        messages.success(request, "Başarılı bir şekilde oluşturuldu", extra_tags="mesaj-başarili")
        return HttpResponseRedirect(post.get_absolute_url())
    
    context = {"form":form}
    return render(request, "post/create.html",context)

def post_delete(request,id):
    post = get_object_or_404(Post,id=id)
    post.delete()
    return redirect("post:index")