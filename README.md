## Personality_Predictor_from_Text

User types a few sentences about themselves. Using keyword extraction and a rule-based scoring system built from scratch, the program maps them to one of the Big Five personality traits with a confidence score and visual bar chart.

**Features:**
- Text input prompt where user writes freely about themselves
- Keyword extraction engine matching words to Big Five dimensions (Openness, Conscientiousness, Extraversion, Agreeableness, Neuroticism)
- Rule-based scoring with weighted keyword matching and negation handling
- Confidence score per trait (0-100%)
- Bar chart visualization of full personality profile
- Breakdown view showing which words contributed to each trait score

**Masters Skills:**
- Keyword-based text classification from scratch
- Rule-based scoring systems and weight tuning
- Feature extraction from unstructured text
- Data visualization for multi-dimensional results

**Tools:**
- `nltk` — tokenization, stemming, stop word removal
- `re` — text cleaning and pattern matching
- `matplotlib` — personality profile bar charts
- `collections` — word frequency counting
- `json` — keyword-to-trait mapping storage

