from django.shortcuts import render, HttpResponse

# Create your views here.
def home_view(request):
    if request.user.is_authenticated():
        context = {"name":"Ali"}
        return render(request, "home.html",context)
    else:
        context = {"name":"Misafir"}
        return render(request, "home.html",context)
