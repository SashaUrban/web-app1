from django.db import models

# Create your models here.


class Article (models.Model):
    THEME_CHOICES = [
        ("Sc", "Science"),
        ("Pol", "Politics"),
        ("Cul", "Culture")
    ]
    name = models.CharField(max_length=200)
    theme = models.CharField(max_length=8, choices=THEME_CHOICES)
    text = models.TextField(null=True)
    author = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Commentary (models.Model):
    text = models.CharField(max_length=4000)
    author = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    article = models.ForeignKey('Article', on_delete=models.PROTECT)

    def __str__(self):
        return self.text
