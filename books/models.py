from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name
    
class Book(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    number_of_pages = models.PositiveBigIntegerField(default=1)

    def __str__(self) -> str:
        return self.title
