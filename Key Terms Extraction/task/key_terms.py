from xml_read import parse_xml
from pipeline import process_news


def main():
    news_list = parse_xml()
    process_news(news_list)
    print(*news_list, sep='\n\n')


if __name__ == '__main__':
    main()
