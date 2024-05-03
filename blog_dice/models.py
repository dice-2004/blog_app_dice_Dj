from django.db import models

class coments(models.Model):
    name = models.CharField(max_length=20)
    slug = models.SlugField()
    coment = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
