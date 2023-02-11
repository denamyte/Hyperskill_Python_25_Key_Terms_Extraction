from xml_read import parse_xml
from tokens import tokenize_and_count


def main():
    news_lst = parse_xml()
    for news in news_lst:
        news.most_common = tokenize_and_count(news.text)
    print(*news_lst, sep='\n\n')


if __name__ == '__main__':
    main()
