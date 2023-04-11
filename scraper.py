import requests
from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright

def get_citations_needed_count(url_input):
    count = 0

    # Get html
    soup = get_html(url_input)

    # Get list of all paragraphs
    paragraphs = soup.find_all("p")

    # Loop: find any paragraph with this opening tag:
    # <a href="/wiki/Wikipedia:Citation_needed" title="Wikipedia:Citation needed">
    for paragraph in paragraphs:
        if paragraph.find_all(attrs={"title":"Wikipedia:Citation needed"}):
            count += 1

    return count

def get_citations_needed_report(url_input):
    citation_report = []

    # Get html
    soup = get_html(url_input)

    # Get list of all paragraphs
    paragraphs = soup.find_all("p")

    # Loop: find any paragraph with this opening tag:
    # <a href="/wiki/Wikipedia:Citation_needed" title="Wikipedia:Citation needed">
    for paragraph in paragraphs:
        if paragraph.find_all(attrs={"title":"Wikipedia:Citation needed"}):
            citation_report.append(paragraph.getText())

    return list_to_string(citation_report)

def get_html(url_input):
    req = requests.get(url_input)
    markup = req.text # converts html request to text
    soup = BeautifulSoup(markup, 'html.parser') # converts to BeautifulSoup readible format
    return soup

def list_to_string(list_input):
    string = ''
    for item in list_input:
        string += item + "\n"
    return string

if __name__ == "__main__":
    url = 'https://en.wikipedia.org/wiki/Geno_Smith'
    # url = 'https://en.wikipedia.org/wiki/WWE'
    # url = 'https://en.wikipedia.org/wiki/History_of_Mexico'
    print(get_citations_needed_report(url))