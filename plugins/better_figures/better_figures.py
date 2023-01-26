from pelican import signals, contents
from bs4 import BeautifulSoup

def better_figures(content):
    if isinstance(content, contents.Static):
        return

    soup = BeautifulSoup(content._content, 'html.parser')

    for image in soup.findAll('img'):
        if image.parent.name == 'figure': continue
        if 'gemoji' in image.get('class', []): continue

        image['class'] = image.get('class', []) + ['figure-img', 'img-fluid', 'rounded']

        if image.get('alt', '') == '' and image.get('title', '') != '': image['alt'] = image['title']
        if image.get('title', '') == '' and image.get('alt', '') != '': image['title'] = image['alt']

        image.wrap(soup.new_tag('figure', **{'class': 'figure'}))
        figure = image.parent

        figcaption = soup.new_tag('figcaption', **{'class': ['figure-caption', 'text-center']})
        figcaption.string = image.get('title', '')
        figure.append(figcaption)

        figure.wrap(soup.new_tag('div', **{'class': 'text-center'}))

    soup.renderContents()
    content._content = soup.decode()

def register():
    signals.content_object_init.connect(better_figures)
