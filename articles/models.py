from django.db import models


# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=300, verbose_name="Заголовок")
    content = models.TextField(verbose_name="Контент")

    def __str__(self):
        return self.title
