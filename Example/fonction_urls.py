from bs4 import BeautifulSoup
import requests
import re

def url_add_http(url):
    """ 
    Add https:// on url if it does not contain one
    """
    string_r = r"^(https://)"
    string_e = re.compile(string_r)
    if not string_e.search(url):
        url = f"https://{url}"
    return url


def reformat_url(url):
    """ reformat the domain name to get base url"""
    url_split = url.split(".")
    return f"{url_split[-2]}.{url_split[-1]}"

def get_url(url):
    """ get url with which the page content will be parsed """
    if not url_test(url):
        url = reformat_url(url)
    url = url_add_http(url)
    return url

def url_test(url):
    """ Allows to test a url and to know if url has a status code of 200 """
    
    # msg of redirection
    redi_text = "If you are not redirected automatically, follow the www.ioam.de"
    
    headers = {
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/109.0"}

    # increase of max_redirect
    #session = requests.Session()
    #session.max_redirects = 100000000000
    try:
        url = url_add_http(url)
        response = requests.get(url, timeout=60, headers= headers)
    except Exception:
        # if max_redirects has been exceeded
        response = requests.get(url, timeout=60, headers= headers, allow_redirects=False)
    
    # if the page content contains a redirection message to another site    
    soup = BeautifulSoup(response.text, "html.parser")
    tags = soup.find_all("body")
    header = soup.find_all("head")
    content = [" ".join(tag.stripped_strings) for tag in tags]
    content = " ".join(content).split(" ")[:-1]
    redi_text = redi_text.split(" ")[:-1]

    return set(content) != set(redi_text) and response.status_code == 200 and header != []