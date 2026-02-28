import json

TRAITS = [
    "openness", "conscientiousness", "extraversion",
    "agreeableness", "neuroticism",
]

NEGATION_WORDS = {
    "not", "no", "never", "don", "don't", "doesn",
    "doesn't", "didn", "didn't", "won", "won't",
    "can't", "cannot", "couldn", "couldn't", "shouldn",
    "shouldn't", "isn", "isn't", "aren", "aren't",
}

SCORE_CEILING = 20


def load_lexicon(path="data/keywords.json"):
    """Load the stem-to-weight keyword lexicon from JSON."""
    with open(path) as f:
        return json.load(f)


def score(stems, originals, lexicon):
    """Score preprocessed tokens against the keyword lexicon.

    Returns dict with keys: scores, contributions, dominant.
    """
    raw_scores = {t: 0 for t in TRAITS}
    contributions = {t: [] for t in TRAITS}

    for i, stem in enumerate(stems):
        for trait in TRAITS:
            if stem in lexicon[trait]:
                weight = lexicon[trait][stem]

                # negation check: look back 1-2 positions
                negated = False
                for j in range(max(0, i - 2), i):
                    if originals[j] in NEGATION_WORDS:
                        negated = True
                        break

                score_delta = -weight if negated else weight
                raw_scores[trait] += score_delta
                contributions[trait].append((originals[i], score_delta))

    # normalize to 0-100%
    scores = {}
    for t in TRAITS:
        clamped = max(raw_scores[t], 0)
        scores[t] = min(int((clamped / SCORE_CEILING) * 100), 100)

    dominant_trait = max(scores, key=scores.get)
    dominant = (dominant_trait, scores[dominant_trait])

    return {
        "scores": scores,
        "contributions": contributions,
        "dominant": dominant,
    }
