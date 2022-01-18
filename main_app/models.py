from django.db import models
from django.urls import reverse

# Create your models here.
EDITIONS = (
    ('F', 'First'),
    ('L', 'Limited'),
    ('A', 'Autographed'),
)

class Author(models.Model):
    name = models.CharField(max_length=50)
    birth_year = models.IntegerField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('authors_detail', kwargs={'pk': self.id})

class Book(models.Model):
    name = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    date_published = models.IntegerField()
    author = models.ManyToManyField(Author)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'book_id': self.id})

class Reprint(models.Model):
    date = models.DateField('Reprint Date')
    edition_type = models.CharField(
        max_length=1,
        choices=EDITIONS,
        default=EDITIONS[0][0],
        )

    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_edition_type_display()} on {self.date}"

    class Meta:
        ordering = ['-date']


