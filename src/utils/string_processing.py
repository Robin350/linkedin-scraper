import logging
import difflib


logger = logging.getLogger(__name__)


def generate_ngrams(text, ngram_sizes):
    text_split = text.split()
    ngrams = []
    for size in ngram_sizes:
        ngrams.extend([
            " ".join(text_split[i:i + size]) for i in range(len(text_split) - size + 1)
        ])
    return ngrams


def ngram_has_keyword(ngrams, keywords, cutoff=0.95):
    for kw in keywords:
        match = difflib.get_close_matches(kw, ngrams, cutoff=cutoff)
        if match:
            return True
    return False


def check_text_matches_a_keyword(text, keywords):
    text_ngrams = generate_ngrams(text, ngram_sizes=[1, 2, 3, 4])
    has_keyword = ngram_has_keyword(text_ngrams, keywords)
    return has_keyword


def get_all_found_keywords(text, keywords):
    found_keywords = []
    for keyword in keywords:
        found = difflib.get_close_matches(keyword.lower(), text.lower().split(' '), cutoff=0.95)
        if found:
            found_keywords.append(keyword)
