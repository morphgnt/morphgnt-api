from django.conf.urls import url

urlpatterns = [
    url(r"^v0/word/(?P<word_id>\d{11}).json$", "morphgnt_api.views.word", name="word"),

    url(r"^v0/paragraph/(?P<paragraph_id>\d{5}).json$", "morphgnt_api.views.paragraph", name="paragraph"),
    url(r"^v0/sentence/(?P<sentence_id>\d{6}).json$", "morphgnt_api.views.sentence", name="sentence"),
    url(r"^v0/verse/(?P<verse_id>\d{6}).json$", "morphgnt_api.views.verse", name="verse"),

    url(r"^v0/book/(?P<book_osis_id>\w+).json$", "morphgnt_api.views.book", name="book"),

    url(r"^v0/root.json$", "morphgnt_api.views.root", name="root"),
]
