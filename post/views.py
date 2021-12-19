from django.shortcuts import render, HttpResponse

# Create your views here.

# Her bir sayfanın html dosyası oluşturulacak.

def post_index(requset):
    return HttpResponse("<b>Post Indeks Sayfası</b>")

def post_detail(requset):
    return HttpResponse("<b>Post Detay Sayfası</b>")

def post_create(requset):
    return HttpResponse("<b>Post Oluşturma Sayfası</b>")

def post_update(requset):
    return HttpResponse("<b>Post Güncelleme Sayfası</b>")

def post_delete(requset):
    return HttpResponse("<b>Post Silme Sayfası</b>")