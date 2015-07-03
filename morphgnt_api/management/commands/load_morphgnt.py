from django.core.management.base import BaseCommand

from morphgnt_api.models import Word, Book, Paragraph, Sentence, Verse


def u(s):
    return s.decode("utf-8")


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


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument("filename", help="filename to import")

    def handle(self, *args, **options):
        filename = options["filename"]

        for k, v in books_by_osis_id.items():
            Book(
                book_osis_id=k,
                name=v[0],
                sblgnt_id=v[1],
            ).save()

        prev_verse = None
        prev_sentence = None
        prev_paragraph = None

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
                    head=head if head != "None" else None,
                ).save()

                if prev_verse is None:
                    prev_verse = Verse(
                        verse_id=verse_id,
                        book_osis_id=books_by_sblgnt_id[int(verse_id[:2])],
                        prev_verse=None,
                        next_verse=None,
                    )
                    prev_verse.save()
                elif prev_verse.verse_id != verse_id:
                    if prev_verse.verse_id[:2] == verse_id[:2]:
                        prev_verse.next_verse = verse_id
                        prev_verse.save()
                    prev_verse = Verse(
                        verse_id=verse_id,
                        book_osis_id=books_by_sblgnt_id[int(verse_id[:2])],
                        prev_verse=prev_verse.verse_id,
                        next_verse=None,
                    )
                    prev_verse.save()

                if prev_sentence is None:
                    prev_sentence = Sentence(
                        sentence_id=sentence_id,
                        book_osis_id=books_by_sblgnt_id[int(sentence_id[:2])],
                        prev_sentence=None,
                        next_sentence=None,
                    )
                    prev_sentence.save()
                elif prev_sentence.sentence_id != sentence_id:
                    if prev_sentence.sentence_id[:2] == sentence_id[:2]:
                        prev_sentence.next_sentence = sentence_id
                        prev_sentence.save()
                    prev_sentence = Sentence(
                        sentence_id=sentence_id,
                        book_osis_id=books_by_sblgnt_id[int(sentence_id[:2])],
                        prev_sentence=prev_sentence.sentence_id,
                        next_sentence=None,
                    )
                    prev_sentence.save()

                if prev_paragraph is None:
                    prev_paragraph = Paragraph(
                        paragraph_id=paragraph_id,
                        book_osis_id=books_by_sblgnt_id[int(paragraph_id[:2])],
                        prev_paragraph=None,
                        next_paragraph=None,
                    )
                    prev_paragraph.save()
                elif prev_paragraph.paragraph_id != paragraph_id:
                    if prev_paragraph.paragraph_id[:2] == paragraph_id[:2]:
                        prev_paragraph.next_paragraph = paragraph_id
                        prev_paragraph.save()
                    prev_paragraph = Paragraph(
                        paragraph_id=paragraph_id,
                        book_osis_id=books_by_sblgnt_id[int(paragraph_id[:2])],
                        prev_paragraph=prev_paragraph.paragraph_id,
                        next_paragraph=None,
                    )
                    prev_paragraph.save()
