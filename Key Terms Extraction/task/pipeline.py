import string
from collections import Counter
from typing import List

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk import WordNetLemmatizer

STOPWORDS = stopwords.words('english')
lemma = WordNetLemmatizer()


def tokenize_and_pipeline(text: str) -> List[str]:
    tokens = sorted(word_tokenize(text.lower()), reverse=True)
    tokens = filter(remain_token, tokens)
    tokens = (map(lemma.lemmatize, tokens))
    tokens = filter(lambda t: len(t) > 1, tokens)
    mc = Counter(tokens).most_common(5)
    return [tpl[0] for tpl in mc]


def remain_token(token: str) -> bool:
    return not token.startswith("'") \
           and token not in STOPWORDS \
           and token not in string.punctuation
