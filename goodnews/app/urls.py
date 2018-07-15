from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:book>/<int:chapter>/<int:verse_num>', views.verse, name='verse'),
]