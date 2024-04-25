import os
import trafilatura
from requests import get


def get_text_from_url(url: str) -> str | None:
    downloaded = trafilatura.fetch_url(url)
    return trafilatura.extract(downloaded)


def get_title_from_url(url: str) -> str:
    try:
        request = get(url)
    except:
        return ''
    if request.status_code != 200:
        return ''
    raw_html = request.text

    start_pos = raw_html.rfind('<h1')
    end_pos = raw_html.rfind('</h1')

    if start_pos == -1 or end_pos == -1 or start_pos >= end_pos:
        return ''

    raw_html = raw_html[start_pos:end_pos]

    start_pos = raw_html.find('>') + 1

    return raw_html[start_pos:].strip()


def make_news_text_file(title: str | None, url: str) -> str | None:
    content = get_text_from_url(url)

    if content is None:
        return None

    if title is None:
        title = get_title_from_url(url)

    if title != '':
        file_title = title.replace(' ', '_')
    else:
        file_title = 'NOT_FOUND_TILE'

    file_path = f'files/{file_title}.txt'
    text = (title.strip() + '\n\n' + content.strip()).strip()

    with open(file_path, 'w') as file:
        file.write(text)

    return file_path


def get_text_from_file(filepath: str) -> str:
    with open(filepath, 'r') as f:
        text = f.read()
    os.remove(filepath)

    return text


print(get_title_from_url('https://rais.tatarstan.ru/index.htm/news/2300098.htm'))