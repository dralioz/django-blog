from django.urls import path
from .views import *

global app_name 
app_name = "post"

urlpatterns = [
    path("index/", post_index),
    path("<int:id>", post_detail, name = "detail"),
    path("create/", post_create),
    path("update/", post_update),
    path("delete/", post_delete),
]
