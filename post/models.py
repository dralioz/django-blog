from django.db import models
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    # Postun sahip olabileceği bir kaç özellikler.
    title = models.CharField(max_length = 120, verbose_name = "Başlık")
    content = models.TextField(verbose_name = "İçerik")
    publishing_date = models.DateTimeField(verbose_name = "Yayınlanma Tarihi")

    def __str__(self):
        # Postun kendi adıyla listede görünmesini sağlar.
        return self.title
    
    def get_absolute_url(self):
        return reverse("post:detail",kwargs={"id":self.id})
