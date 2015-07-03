from django.core.urlresolvers import reverse
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, get_list_or_404

from morphgnt_api.models import Word


def word(request, word_id):
    w = get_object_or_404(Word, word_id=word_id)
    return JsonResponse(w.to_dict())


def paragraph(request, paragraph_id):
    words = get_list_or_404(Word, paragraph_id=paragraph_id)
    return JsonResponse({
        "@id": reverse("paragraph", args=[paragraph_id]),
        "@type": "paragraph",
        "words": [w.to_dict() for w in words],
    })


def sentence(request, sentence_id):
    words = get_list_or_404(Word, sentence_id=sentence_id)
    return JsonResponse({
        "@id": reverse("sentence", args=[sentence_id]),
        "@type": "sentence",
        "words": [w.to_dict() for w in words],
    })


def verse(request, verse_id):
    words = get_list_or_404(Word, verse_id=verse_id)
    return JsonResponse({
        "@id": reverse("verse", args=[verse_id]),
        "@type": "verse",
        "words": [w.to_dict() for w in words],
    })
