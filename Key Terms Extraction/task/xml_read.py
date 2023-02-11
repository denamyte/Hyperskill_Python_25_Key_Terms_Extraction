from typing import List

from lxml import etree
from data import News


def parse_xml() -> List[News]:
    tree = etree.parse('news.xml')
    corpus = tree.getroot()[0]
    return [News(item[0].text, item[1].text) for item in corpus]
