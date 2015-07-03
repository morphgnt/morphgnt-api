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
