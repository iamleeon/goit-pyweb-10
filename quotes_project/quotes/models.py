from django.db import models


# Create your models here.
class Author(models.Model):
    fullname = models.CharField(max_length=100, null=False, unique=True)
    born_date = models.CharField(null=False)
    born_location = models.CharField(null=False)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.fullname}"


class Tag(models.Model):
    name = models.CharField(max_length=150, null=False, unique=True)


class Quote(models.Model):
    quote = models.TextField(null=False)
    tags = models.ManyToManyField(Tag)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, default=None, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.quote}"
