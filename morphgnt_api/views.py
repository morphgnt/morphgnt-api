from django.core.urlresolvers import reverse
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404

from morphgnt_api.models import Word, Book, Verse, Paragraph, Sentence


def resource_view(model):
    def _(request, **kwargs):
        response = JsonResponse(get_object_or_404(model, **kwargs).to_dict())
        response["Access-Control-Allow-Origin"] = "*"
        return response
    return _


word = resource_view(Word)
paragraph = resource_view(Paragraph)
sentence = resource_view(Sentence)
verse = resource_view(Verse)
book = resource_view(Book)


def root(request):
    response = JsonResponse({
        "books": [
            {
                "@id": reverse("book", args=[book.book_osis_id]),
                "name": book.name,
            }
            for book in Book.objects.order_by("sblgnt_id")
        ]
    })
    response["Access-Control-Allow-Origin"] = "*"
    return response


def home(request):
    return HttpResponse("Go to <a href='{link}'>{link}</a> for API. See <a href='https://github.com/morphgnt/morphgnt-api'>https://github.com/morphgnt/morphgnt-api</a> for documentation.".format(link=reverse("root")), content_type="text/html")


def loader_verification(request):
    return HttpResponse("loaderio-97c892ba1d7ce63eb626ca62a7a0a961")
