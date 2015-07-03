from django.core.urlresolvers import reverse
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404

from morphgnt_api.models import Word, Book, Verse, Paragraph, Sentence


def resource_view(model):
    def _(request, **kwargs):
        return JsonResponse(get_object_or_404(model, **kwargs).to_dict())
    return _


word = resource_view(Word)
paragraph = resource_view(Paragraph)
sentence = resource_view(Sentence)
verse = resource_view(Verse)
book = resource_view(Book)


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


def home(request):
    return HttpResponse("see <a href='{link}'>{link}</a>.".format(link=reverse("root")), content_type="text/html")
