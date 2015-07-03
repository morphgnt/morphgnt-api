# morphgnt-api

an experimental REST API for MorphGNT

This will go up on `api.morphgnt.org` shortly.

Note that the `/v0/` prefix is used because there is no commitment to keep
this API. It is subject to rapid change at the moment.

The URI patterns are:

```
/v0/word/{word_id}.json
/v0/paragraph/{paragraph_id}.json
/v0/sentence/{sentence_id}.json
/v0/verse/{verse_id}.json
/v0/book/{osis_id}.json
```

A word (currently) looks something like this:

```
{
    @id: "/v0/word/64001001005.json",
    verse_id: "/v0/verse/640101.json",
    sentence_id: "/v0/sentence/640001.json",
    paragraph_id: "/v0/paragraph/64001.json",
    crit_text: "λόγος,",
    text: "λόγος,",
    word: "λόγος",
    norm: "λόγος",
    lemma: "λόγος",
    pos: "N",
    case: "N",
    number: "S",
    gender: "M",
    dep_type: "S",
    head: "/v0/word/64001001002.json"
}
```


A verse (currently) looks something like this:

```
{
    @id: "/v0/verse/640101.json",
    @type: "verse",
    book: "/v0/book/John.json",
    words: [...]
}
```

where `words` is a list of objects like the word above.

A paragraph and sentence are very similar to a verse (with an `@id`, `@type`
and `words` list).

A book (currently) looks something like this:

```
{
    "@id": "/v0/book/1Cor.json",
    "@type": "book",
    "name": "1 Corinthians",
    "first_paragraph": "/v0/paragraph/67001.json",
    "first_verse": "/v0/verse/670101.json",
    "first_sentence": "/v0/sentence/670001.json"
}
```

Feedback is greatly appreciated to make this more useful.

Things that still need to be done include:

* prev/next navigation between paragraphs, sentences and verses
* investigation of vocabulary re-use
