from django.db import models

# Create your models here.
class Verse(models.Model):
    book_name = models.CharField(max_length=100)
    book_abbr = models.CharField(max_length=10)
    chapter_number = models.IntegerField()
    verse_number = models.IntegerField()
    verse_text = models.TextField()

class Tag(models.Model):
    tag_name = models.CharField(max_length=100)
    verse = models.ManyToManyField(Verse)  # Django creates the join table automatically
