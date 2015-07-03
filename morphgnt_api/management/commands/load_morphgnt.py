from django.core.management.base import BaseCommand

from morphgnt_api.models import Word


def u(s):
    return s.decode("utf-8")


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument("filename", help="filename to import")

    def handle(self, *args, **options):
        filename = options["filename"]

        last_book = None
        with open(filename, "rb") as f:
            for line in f:
                word_id, verse_id, paragraph_id, sentence_id, \
                    pos, parse, \
                    crit_text, text, word, norm, lemma, \
                    dep_type, head = line.strip().split()

                Word(
                    word_id=word_id,
                    verse_id=verse_id,
                    paragraph_id=paragraph_id,
                    sentence_id=sentence_id,
                    pos=pos,
                    parse=parse,
                    crit_text=u(crit_text),
                    text=u(text),
                    word=u(word),
                    norm=u(norm),
                    lemma=u(lemma),
                    dep_type=dep_type,
                    head=head
                ).save()

                if verse_id[:2] != last_book:
                    print verse_id[:2]
                    last_book = verse_id[:2]
