from django.shortcuts import get_object_or_404, render, HttpResponse
from .models import Post

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
    return render(request, "post/create.html",{})

def post_update(request):
    return render(request, "post/update.html",{})

def post_delete(request):
    return render(request, "post/delete.html",{})