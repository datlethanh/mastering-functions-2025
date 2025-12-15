from nlplogic.corenlp import (
    search_wikipedia,
    summarize_wikipedia,
    get_text_blob,
    get_phrases,
)


def test_get_phrases():
    assert "duolingo" in get_phrases("Duolingo English Test")

def test_search_wikipedia():
    assert "DET" in search_wikipedia("Duolingo English Test")

def test_summarize_wikipedia():
    assert "to be proficient in English" in summarize_wikipedia("Duolingo English Test")

def test_get_text_blob():
    assert "" in get_text_blob("Duolingo English Test")
