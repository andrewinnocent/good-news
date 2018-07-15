from django.shortcuts import render
from django.http import HttpResponse
from .models import Verse


# homepage (/app)
def index(request):
    return render(request, "index.html")


# def chapter(request, book, chapter):
#     pass


def verse(request, book, chapter, verse_num):

    #verse = get_verse(book, chapter, verse_num)
    #tags = get_tags_by_verse(verse)
    #all_tags = get_all_tags()
    #res = {
    #    'verse': verse,
    #    'verse_tags': tags,
    #    'all_tags': all_tags,
    #}


    v = Verse.objects.get(book_name=book, chapter_number=chapter, verse_number=verse_num)
    print("verse : ", v)
    res = {"verse": v}
    return render(request, "verse.html", res)
