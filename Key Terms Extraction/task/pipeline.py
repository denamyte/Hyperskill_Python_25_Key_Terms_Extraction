import string
from collections import Counter

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tag import pos_tag

from data import News

lemma = WordNetLemmatizer()
EXCLUDED = set(stopwords.words('english') + list(string.punctuation)
               + ['people'])


def tokenize_and_pipeline(news: News):
    tokens = word_tokenize(news.text.lower())
    tokens = [t for t in tokens if remain_token(t)]
    tokens = [lemma.lemmatize(t) for t in tokens]
    tagged = pos_tag(tokens)
    nouns = [w for w, tag in tagged if tag.startswith('NN')]
    sorted_nouns = sorted(nouns, reverse=True)
    counter = Counter(sorted_nouns)
    mc = counter.most_common(5)
    news.most_common = [tpl[0] for tpl in mc]


def remain_token(token: str) -> bool:
    return not token.startswith("'") \
           and len(token) > 1 \
           and token not in EXCLUDED
