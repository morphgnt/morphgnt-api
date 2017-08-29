import json

from django.core.urlresolvers import reverse
from django.db import connection
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404

from morphgnt_api.models import Word, Book, Verse, Paragraph, Sentence

from . import ref


def resource_view(model):
    def _(request, **kwargs):
        response = JsonResponse(get_object_or_404(model, **kwargs).to_dict())
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
                "osis": book.book_osis_id,
                "name": book.name,
            }
            for book in Book.objects.order_by("sblgnt_id")
        ]
    })
    return response


def verse_lookup(request):
    try:
        verse = ref.verse(list(request.GET.keys())[0])
    except ValueError as e:
        response = JsonResponse({"message": str(e)}, status=400)
    else:
        verse_id = f"{verse.book_num+60:02d}{verse.chapter_num:02d}{verse.verse_num:02d}"
        response = JsonResponse({
            "verse_id": reverse("verse", args=[verse_id]),
        })
    return response


def frequency(request):

    payload = json.loads(request.body)
    output = []

    lemmas = [item["lemma"] for item in payload["input"]]

    cursor = connection.cursor()
    cursor.execute("select lemma, count(*) from morphgnt_api_word where lemma IN %s group by lemma", (tuple(lemmas),))
    counts = dict(cursor.fetchall())

    for item in payload["input"]:
        id_, lemma = item["id"], item["lemma"]
        lemma_count = counts[lemma]
        output.append({"id": id_, "count": lemma_count})

    return JsonResponse({"output": output})


def kwic(request):
    try:
        word = list(request.GET.keys())[0]
    except ValueError as e:
        response = JsonResponse({"message": str(e)}, status=400)
    else:
        words = list(Word.objects.filter(
            verse_id__in=Word.objects.filter(word=word).values("verse_id")
        ).values_list("text", "word", "verse_id"))

        results = []

        for index, item in enumerate(words):
            if item[1] == word:
                pre = []
                post = []
                for i in range(max(0, index - 5), index):
                    if words[i][2] == item[2]:
                        pre.append(words[i][0])
                for i in range(index + 1, min(len(words), index + 6)):
                    if words[i][2] == item[2]:
                        post.append(words[i][0])

                results.append({
                    "verse_id": reverse("verse", args=[item[2]]),
                    "title": ref.verse_from_bcv(item[2]).title,
                    "pre": " ".join(pre),
                    "keyword": item[0],
                    "post": " ".join(post),
                })

        response = JsonResponse({
            "word": word,
            "results": results,
        })
    return response


def home(request):
    return HttpResponse("Go to <a href='{link}'>{link}</a> for API. See <a href='https://github.com/morphgnt/morphgnt-api'>https://github.com/morphgnt/morphgnt-api</a> for documentation.".format(link=reverse("root")), content_type="text/html")


def loader_verification(request):
    return HttpResponse("loaderio-97c892ba1d7ce63eb626ca62a7a0a961")
