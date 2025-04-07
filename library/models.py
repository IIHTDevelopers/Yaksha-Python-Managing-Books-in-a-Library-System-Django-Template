from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200, unique=True)
    author = models.CharField(max_length=100)
    published_date = models.DateField()
    isbn = models.CharField(max_length=13, unique=True)
    available_copies = models.IntegerField(default=1)

    def __str__(self):
        return self.title