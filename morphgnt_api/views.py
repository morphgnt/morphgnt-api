from django.core.urlresolvers import reverse
from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from morphgnt_api.models import Word, Book, Verse, Paragraph, Sentence


def word(request, word_id):
    w = get_object_or_404(Word, word_id=word_id)
    return JsonResponse(w.to_dict())


def paragraph(request, paragraph_id):
    p = get_object_or_404(Paragraph, paragraph_id=paragraph_id)
    return JsonResponse(p.to_dict())


def sentence(request, sentence_id):
    s = get_object_or_404(Sentence, sentence_id=sentence_id)
    return JsonResponse(s.to_dict())


def verse(request, verse_id):
    v = get_object_or_404(Verse, verse_id=verse_id)
    return JsonResponse(v.to_dict())


def book(request, book_osis_id):
    b = get_object_or_404(Book, book_osis_id=book_osis_id)
    return JsonResponse(b.to_dict())


def root(request):
    return JsonResponse({
        "books": [
            {
                "@id": reverse("book", args=[book.book_osis_id]),
                "name": book.name,
            }
            for book in Book.objects.order_by("sblgnt_id")
        ]
    })
