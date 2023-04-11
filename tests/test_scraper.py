import pytest
import scraper

def test_exists():
    assert scraper.get_citations_needed_count('https://en.wikipedia.org/wiki/Geno_Smith')

# @pytest.mark.skip("TODO")
def test_citation_count():
    actual = scraper.get_citations_needed_count('https://en.wikipedia.org/wiki/Geno_Smith')
    expected = 1
    assert actual == expected

# @pytest.mark.skip("TODO")
def test_citation_count_WWE():
    actual = scraper.get_citations_needed_count('https://en.wikipedia.org/wiki/WWE')
    expected = 2
    assert actual == expected
