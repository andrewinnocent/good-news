from django.urls import path

from . import views

urlpatterns = [
    # /app
    path('', views.index, name='index'),

    # /app/Genesis/1
    # path('<str:book>/<int:chapter>', views.chapter_number, name='chapter'),

    # /app/Genesis/1/5
    path('<str:book>/<int:chapter>/<int:verse_num>', views.verse, name='verse')
]
