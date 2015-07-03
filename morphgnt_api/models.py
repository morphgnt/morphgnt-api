from django.core.urlresolvers import reverse
from django.db import models


def parse_as_dict(parse):
    return {
        label: parse[i]
        for i, label in enumerate([
            "person", "tense", "voice", "mood", "case", "number", "gender", "degree"
        ])
        if parse[i] != "-"
    }


class Word(models.Model):

    word_id = models.CharField(max_length=11)
    verse_id = models.CharField(max_length=6)
    paragraph_id = models.CharField(max_length=5)
    sentence_id = models.CharField(max_length=6)
    pos = models.CharField(max_length=2)
    parse = models.CharField(max_length=8)

    crit_text = models.CharField(max_length=50)
    text = models.CharField(max_length=50)
    word = models.CharField(max_length=50)
    norm = models.CharField(max_length=50)
    lemma = models.CharField(max_length=50)

    dep_type = models.CharField(max_length=4)
    head = models.CharField(max_length=11, null=True)

    def to_dict(self):
        d = {
            "@id": reverse("word", args=[self.word_id]),
            "verse_id": reverse("verse", args=[self.verse_id]),
            "paragraph_id": reverse("paragraph", args=[self.paragraph_id]),
            "sentence_id": reverse("sentence", args=[self.sentence_id]),
            "pos": self.pos.strip("-"),
            "crit_text": self.crit_text,
            "text": self.text,
            "word": self.word,
            "norm": self.norm,
            "lemma": self.lemma,
            "dep_type": self.dep_type,
            "head": reverse("word", args=[self.head]) if self.head else None,
        }
        d.update(parse_as_dict(self.parse))
        return d


class Paragraph(models.Model):

    paragraph_id = models.CharField(max_length=5)
    book_osis_id = models.CharField(max_length=6)
    prev_paragraph = models.CharField(max_length=5, null=True)
    next_paragraph = models.CharField(max_length=5, null=True)

    def to_dict(self):
        return {
            "@id": reverse("paragraph", args=[self.paragraph_id]),
            "@type": "paragraph",
            "book": reverse("book", args=[self.book_osis_id]),
            "words": [w.to_dict() for w in Word.objects.filter(paragraph_id=self.paragraph_id).order_by("word_id")],
        }


class Sentence(models.Model):

    sentence_id = models.CharField(max_length=6)
    book_osis_id = models.CharField(max_length=6)
    prev_sentence = models.CharField(max_length=6, null=True)
    next_sentence = models.CharField(max_length=6, null=True)

    def to_dict(self):
        return {
            "@id": reverse("sentence", args=[self.sentence_id]),
            "@type": "sentence",
            "book": reverse("book", args=[self.book_osis_id]),
            "words": [w.to_dict() for w in Word.objects.filter(sentence_id=self.sentence_id).order_by("word_id")],
        }


class Verse(models.Model):

    verse_id = models.CharField(max_length=6)
    book_osis_id = models.CharField(max_length=6)
    prev_verse = models.CharField(max_length=6, null=True)
    next_verse = models.CharField(max_length=6, null=True)

    def to_dict(self):
        return {
            "@id": reverse("verse", args=[self.verse_id]),
            "@type": "verse",
            "book": reverse("book", args=[self.book_osis_id]),
            "words": [w.to_dict() for w in Word.objects.filter(verse_id=self.verse_id).order_by("word_id")],
        }


class Book(models.Model):

    book_osis_id = models.CharField(max_length=6)
    name = models.CharField(max_length=20)
    sblgnt_id = models.CharField(max_length=2)

    def first_verse(self):
        return Verse.objects.filter(book_osis_id=self.book_osis_id).order_by("verse_id")[0]

    def first_sentence(self):
        return Sentence.objects.filter(book_osis_id=self.book_osis_id).order_by("sentence_id")[0]

    def first_paragraph(self):
        return Paragraph.objects.filter(book_osis_id=self.book_osis_id).order_by("paragraph_id")[0]

    def to_dict(self):
        return {
            "@id": reverse("book", args=[self.book_osis_id]),
            "@type": "book",
            "name": self.name,
            "first_verse": reverse("verse", args=[self.first_verse().verse_id]),
            "first_sentence": reverse("sentence", args=[self.first_sentence().sentence_id]),
            "first_paragraph": reverse("paragraph", args=[self.first_paragraph().paragraph_id]),
        }
