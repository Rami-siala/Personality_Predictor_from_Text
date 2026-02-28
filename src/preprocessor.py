import re
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

NEGATION_WORDS = {
    "not", "no", "never", "neither", "nobody", "nothing",
    "nor", "nowhere", "don", "don't", "doesn", "doesn't",
    "didn", "didn't", "won", "won't", "wouldn", "wouldn't",
    "can't", "cannot", "couldn", "couldn't", "shouldn",
    "shouldn't", "isn", "isn't", "aren", "aren't",
    "wasn", "wasn't", "weren", "weren't", "haven",
    "haven't", "hasn", "hasn't", "hadn", "hadn't",
}

_stop = set(stopwords.words("english"))
_stemmer = PorterStemmer()


def preprocess(text):
    """Take raw user text and return (stems, originals) lists."""

    # a) lowercase and clean — keep letters, spaces, apostrophes
    text = text.lower()
    text = re.sub(r"[^a-z\s']", "", text)

    # b) tokenize
    tokens = word_tokenize(text)

    # c) remove stop words but keep negation words
    filtered = [t for t in tokens if t not in _stop or t in NEGATION_WORDS]

    # d) stem and track originals
    stems = []
    originals = []
    for word in filtered:
        stems.append(_stemmer.stem(word))
        originals.append(word)

    return stems, originals
