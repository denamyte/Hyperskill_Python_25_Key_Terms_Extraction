import string
from typing import List

from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tag import pos_tag
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer

from data import News

lemma = WordNetLemmatizer()
EXCLUDED = set(stopwords.words('english') + list(string.punctuation)
               + ['follow-up', 'binge-watch', 'mid-2009', 'rofl-ing',
                  'other-and', 'two-thirds', 'u', 'tms', 'less', 'disorder',
                  'cities', 'access', 'income', 'value', 'revenue', 'revenues',
                  'price', 'amazon', 'apple', 'shows'])


def process_news(news_list: List[News]):
    dataset: List[str] = []
    for news in news_list:
        tokens = word_tokenize(news.text.lower())
        tokens = [t for t in tokens if remain_token(t)]
        tokens = [lemma.lemmatize(t) for t in tokens]
        tagged = pos_tag(tokens)
        dataset.append(' '.join(w for w, tag in tagged if tag.startswith('NN')))

    vectorizer = TfidfVectorizer()
    matrix = vectorizer.fit_transform(dataset)
    voc = vectorizer.get_feature_names_out()
    array = matrix.toarray()

    for i, news, in enumerate(news_list):
        dic = {voc[idx]: score for idx, score in enumerate(array[i]) if score}
        it = iter(sorted(dic.items(), key=lambda item: (item[1], item[0]),
                         reverse=True))
        news.most_common = [next(it)[0] for _ in range(5)]


def remain_token(token: str) -> bool:
    return not token.startswith("'") \
           and len(token) > 1 \
           and token not in EXCLUDED
