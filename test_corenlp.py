from nlplogic.corenlp import (
    search_wikipedia,
    summarize_wikipedia,
    get_text_blob,
    get_phrases,
)


def test_get_phrases():
    assert "Wynxx" in get_phrases("Wynxx")

def test_search_wikipedia():
    assert "Wynxx" in search_wikipedia("Wynxx")

def test_summarize_wikipedia():
    assert "Wynxx" in summarize_wikipedia("Wynxx")

def test_get_text_blob():
    assert "Wynxx" in get_text_blob("Wynxx")
