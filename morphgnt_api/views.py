from django.core.urlresolvers import reverse
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, get_list_or_404

from morphgnt_api.models import Word


books_by_osis_id = {
    "Matt": ("Matthew", 61),
    "Mark": ("Mark", 62),
    "Luke": ("Luke", 63),
    "John": ("John", 64),
    "Acts": ("Acts", 65),
    "Rom": ("Romans", 66),
    "1Cor": ("1 Corinthians", 67),
    "2Cor": ("2 Corinthians", 68),
    "Gal": ("Galatians", 69),
    "Eph": ("Ephesians", 70),
    "Phil": ("Philippians", 71),
    "Col": ("Colossians", 72),
    "1Thess": ("1 Thessalonians", 73),
    "2Thess": ("2 Thessalonians", 74),
    "1Tim": ("1 Timothy", 75),
    "2Tim": ("2 Timothy", 76),
    "Titus": ("Titus", 77),
    "Phlm": ("Philemon", 78),
    "Heb": ("Hebrews", 79),
    "Jas": ("James", 80),
    "1Pet": ("1 Peter", 81),
    "2Pet": ("2 Peter", 82),
    "1John": ("1 John", 83),
    "2John": ("2 John", 84),
    "3John": ("3 John", 85),
    "Jude": ("Jude", 86),
    "Rev": ("Revelation", 87),
}


books_by_sblgnt_id = {
    v[1]: k
    for k, v in books_by_osis_id.items()
}


def word(request, word_id):
    w = get_object_or_404(Word, word_id=word_id)
    return JsonResponse(w.to_dict())


def paragraph(request, paragraph_id):
    words = get_list_or_404(Word, paragraph_id=paragraph_id)
    return JsonResponse({
        "@id": reverse("paragraph", args=[paragraph_id]),
        "@type": "paragraph",
        "book": reverse("book", args=[books_by_sblgnt_id[int(paragraph_id[:2])]]),
        "words": [w.to_dict() for w in words],
    })


def sentence(request, sentence_id):
    words = get_list_or_404(Word, sentence_id=sentence_id)
    return JsonResponse({
        "@id": reverse("sentence", args=[sentence_id]),
        "@type": "sentence",
        "book": reverse("book", args=[books_by_sblgnt_id[int(sentence_id[:2])]]),
        "words": [w.to_dict() for w in words],
    })


def verse(request, verse_id):
    words = get_list_or_404(Word, verse_id=verse_id)
    return JsonResponse({
        "@id": reverse("verse", args=[verse_id]),
        "@type": "verse",
        "book": reverse("book", args=[books_by_sblgnt_id[int(verse_id[:2])]]),
        "words": [w.to_dict() for w in words],
    })


def book(request, osis_id):
    return JsonResponse({
        "@id": reverse("book", args=[osis_id]),
        "@type": "book",
        "name": books_by_osis_id[osis_id][0],
        "first_verse": reverse("verse", args=["{}0101".format(books_by_osis_id[osis_id][1])]),
        "first_sentence": reverse("sentence", args=["{}0001".format(books_by_osis_id[osis_id][1])]),
        "first_paragraph": reverse("paragraph", args=["{}001".format(books_by_osis_id[osis_id][1])]),
    })
