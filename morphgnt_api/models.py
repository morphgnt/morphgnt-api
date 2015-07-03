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

    class Meta:
        ordering = ["word_id"]

    @staticmethod
    def get_full_id(word_id):
        return reverse("word", args=[word_id]) if word_id else None

    def to_dict(self):
        d = {
            "@id": Word.get_full_id(self.word_id),
            "@type": "word",
            "verse_id": Verse.get_full_id(self.verse_id),
            "paragraph_id": Paragraph.get_full_id(self.paragraph_id),
            "sentence_id": Sentence.get_full_id(self.sentence_id),
            "pos": self.pos.strip("-"),
            "crit_text": self.crit_text,
            "text": self.text,
            "word": self.word,
            "norm": self.norm,
            "lemma": self.lemma,
            "dep_type": self.dep_type,
            "head": Word.get_full_id(self.head),
        }
        d.update(parse_as_dict(self.parse))
        return d


class Paragraph(models.Model):

    paragraph_id = models.CharField(max_length=5)
    book_osis_id = models.CharField(max_length=6)
    prev_paragraph = models.CharField(max_length=5, null=True)
    next_paragraph = models.CharField(max_length=5, null=True)

    class Meta:
        ordering = ["paragraph_id"]

    @staticmethod
    def get_full_id(paragraph_id):
        return reverse("paragraph", args=[paragraph_id]) if paragraph_id else None

    def words(self):
        return Word.objects.filter(paragraph_id=self.paragraph_id)

    def to_dict(self):
        return {
            "@id": Paragraph.get_full_id(self.paragraph_id),
            "@type": "paragraph",
            "prev": Paragraph.get_full_id(self.prev_paragraph),
            "next": Paragraph.get_full_id(self.next_paragraph),
            "book": Book.get_full_id(self.book_osis_id),
            "words": [w.to_dict() for w in self.words()],
        }


class Sentence(models.Model):

    sentence_id = models.CharField(max_length=6)
    book_osis_id = models.CharField(max_length=6)
    prev_sentence = models.CharField(max_length=6, null=True)
    next_sentence = models.CharField(max_length=6, null=True)

    class Meta:
        ordering = ["sentence_id"]

    @staticmethod
    def get_full_id(sentence_id):
        return reverse("sentence", args=[sentence_id]) if sentence_id else None

    def words(self):
        return Word.objects.filter(sentence_id=self.sentence_id)

    def to_dict(self):
        return {
            "@id": Sentence.get_full_id(self.sentence_id),
            "@type": "sentence",
            "prev": Sentence.get_full_id(self.prev_sentence),
            "next": Sentence.get_full_id(self.next_sentence),
            "book": Book.get_full_id(self.book_osis_id),
            "words": [w.to_dict() for w in self.words()],
        }


class Verse(models.Model):

    verse_id = models.CharField(max_length=6)
    book_osis_id = models.CharField(max_length=6)
    prev_verse = models.CharField(max_length=6, null=True)
    next_verse = models.CharField(max_length=6, null=True)

    class Meta:
        ordering = ["verse_id"]

    @staticmethod
    def get_full_id(verse_id):
        return reverse("verse", args=[verse_id]) if verse_id else None

    def words(self):
        return Word.objects.filter(verse_id=self.verse_id)

    def to_dict(self):
        return {
            "@id": reverse("verse", args=[self.verse_id]),
            "@type": "verse",
            "book": reverse("book", args=[self.book_osis_id]),
            "prev": Verse.get_full_id(self.prev_verse),
            "next": Verse.get_full_id(self.next_verse),
            "words": [w.to_dict() for w in self.words()],
        }


class Book(models.Model):

    book_osis_id = models.CharField(max_length=6)
    name = models.CharField(max_length=20)
    sblgnt_id = models.CharField(max_length=2)

    class Meta:
        ordering = ["sblgnt_id"]

    @staticmethod
    def get_full_id(book_osis_id):
        return reverse("book", args=[book_osis_id]) if book_osis_id else None

    def first_verse(self):
        return Verse.objects.filter(book_osis_id=self.book_osis_id)[0]

    def first_sentence(self):
        return Sentence.objects.filter(book_osis_id=self.book_osis_id)[0]

    def first_paragraph(self):
        return Paragraph.objects.filter(book_osis_id=self.book_osis_id)[0]

    def to_dict(self):
        return {
            "@id": Book.get_full_id(self.book_osis_id),
            "@type": "book",
            "name": self.name,
            "root": reverse("root"),
            "first_verse": Verse.get_full_id(self.first_verse().verse_id),
            "first_sentence": Sentence.get_full_id(self.first_sentence().sentence_id),
            "first_paragraph": Paragraph.get_full_id(self.first_paragraph().paragraph_id),
        }
