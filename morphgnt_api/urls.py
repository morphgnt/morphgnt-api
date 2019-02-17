from django.conf.urls import include, url

from . import views


urlpatterns = [
    url(r"^v0/word/(?P<word_id>\d{11}).json$", views.word, name="word"),

    url(r"^v0/paragraph/(?P<paragraph_id>\d{5}).json$", views.paragraph, name="paragraph"),
    url(r"^v0/sentence/(?P<sentence_id>\d{6}).json$", views.sentence, name="sentence"),
    url(r"^v0/verse/(?P<verse_id>\d{6}).json$", views.verse, name="verse"),

    url(r"^v0/book/(?P<book_osis_id>\w+).json$", views.book, name="book"),

    url(r"^v0/verse-lookup/$", views.verse_lookup, name="verse_lookup"),
    url(r"^v0/frequency/$", views.frequency, name="frequency"),
    url(r"^v0/kwic/$", views.kwic, name="kwic"),

    url(r"^v0/root.json$", views.root, name="root"),

    url(r"^loaderio-97c892ba1d7ce63eb626ca62a7a0a961/$", views.loader_verification),

    url(r"^$", views.home, name="home"),
]
