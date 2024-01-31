from enum import Enum


class BibtexReferenceTypes(Enum):
    article = {
        "type": "article",
        "required_fields": ["author", "title", "journal", "year"],
        "optional_fields": ["volume", "number", "pages", "month", "note"]
    }

    book = {
        "type": "book",
        "required_fields": ["author", "title", "publisher", "year"],
        "optional_fields": ["volume", "number", "series", "address", "edition", "month", "note", "isbn"]
    }

    booklet = {
        "type": "booklet",
        "required_fields": ["title"],
        "optional_fields": ["author", "howpublished", "address", "month", "year", "note"]
    }

    conference = {
        "type": "conference",
        "required_fields": ["author", "title", "booktitle", "year"],
        "optional_fields": ["editor", "volume", "number", "series", "pages", "address", "month", "organization",
                            "publisher", "note"]
    }

    inbook = {
        "type": "inbook",
        "required_fields": ["author", "title", "booktitle", "chapter", "pages", "publisher", "year"],
        "optional_fields": ["volume", "number", "series", "type", "address", "edition", "month", "note"]
    }

    incollection = {
        "type": "incollection",
        "required_fields": ["author", "title", "booktitle", "publisher", "year"],
        "optional_fields": ["editor", "volume", "number", "series", "type", "chapter", "pages", "address", "edition",
                            "month", "note"]
    }

    inproceedings = {
        "type": "inproceedings",
        "required_fields": ["author", "title", "booktitle", "year"],
        "optional_fields": ["editor", "volume", "number", "series", "pages", "address", "month", "organization",
                            "publisher", "note"]
    }

    manual = {
        "type": "manual",
        "required_fields": ["title"],
        "optional_fields": ["author", "organization", "address", "edition", "month", "year", "note"]
    }

    mastersthesis = {
        "type": "mastersthesis",
        "required_fields": ["author", "title", "school", "year"],
        "optional_fields": ["type", "address", "month", "note"]
    }

    thesis = {
        "type": "thesis",
        "required_fields": ["author", "title", "school", "year"],
        "optional_fields": ["type", "address", "month", "note"]
    }

    misc = {
        "type": "misc",
        "required_fields": [],
        "optional_fields": ["author", "title", "howpublished", "month", "year", "note"]
    }

    phdthesis = {
        "type": "phdthesis",
        "required_fields": ["author", "title", "school", "year"],
        "optional_fields": ["type", "address", "month", "note"]
    }

    proceedings = {
        "type": "proceedings",
        "required_fields": ["title", "year"],
        "optional_fields": ["editor", "volume", "number", "series", "address", "month", "organization", "publisher",
                            "note"]
    }

    techreport = {
        "type": "techreport",
        "required_fields": ["author", "title", "institution", "year"],
        "optional_fields": ["type", "number", "address", "month", "note"]
    }

    unpublished = {
        "type": "unpublished",
        "required_fields": ["author", "title", "note"],
        "optional_fields": ["month", "year"]
    }
