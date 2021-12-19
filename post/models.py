from django.db import models

# Create your models here.
class Post(models.Model):
    # Postun sahip olabileceği bir kaç özellikler.
    title = models.CharField(max_length = 120, verbose_name = "Başlık")
    content = models.TextField(verbose_name = "İçerik")
    publishing_date = models.DateTimeField(verbose_name = "Yayınlanma Tarihi")

    def __str__(self):
        # Postun kendi adıyla listede görünmesini sağlar.
        return self.title
