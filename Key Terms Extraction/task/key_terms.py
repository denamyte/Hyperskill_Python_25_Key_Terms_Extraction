from xml_read import parse_xml
from pipeline import tokenize_and_pipeline


def main():
    news_lst = parse_xml()
    for news in news_lst:
        tokenize_and_pipeline(news)
    print(*news_lst, sep='\n\n')


if __name__ == '__main__':
    main()
