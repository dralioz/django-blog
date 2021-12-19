from django.shortcuts import render, HttpResponse

# Create your views here.

# Her bir sayfanın html dosyası oluşturulacak.

def post_index(request):
    return render(request, "post/index.html",{})

def post_detail(request):
    return render(request, "post/detail.html",{})

def post_create(request):
    return render(request, "post/create.html",{})

def post_update(request):
    return render(request, "post/update.html",{})

def post_delete(request):
    return render(request, "post/delete.html",{})