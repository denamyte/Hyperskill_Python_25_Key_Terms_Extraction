from collections import Counter
from typing import List

from nltk.tokenize import word_tokenize
from nltk import download

# download('all')


def tokenize_and_count(text: str) -> List[str]:
    tokens = sorted(word_tokenize(text.lower()), reverse=True)
    counter = Counter(tokens)
    return [tpl[0] for tpl in counter.most_common(5)]
