from bs4 import BeautifulSoup
import pprint
import requests
import re
import bs4

url = "https://livehdcams.com"
#"https://citysmile.ru"
# https://livehdcams.com

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/109.0"}


response = requests.get(url, timeout=60, headers= headers)

if response.status_code != 200:
    print("None")
    print(response.status_code)
else:
    print(response.status_code)
    soup = BeautifulSoup(response.content, "html.parser")
    #links = [elt.getText() for elt in soup.find_all(name="title")]
    
    #links = soup.find_all(lambda tag: (tag.name=='meta') & (tag.has_attr('name') & tag.has_attr('content')))
    #content = [str(tag['content']) for tag in links if tag['name'] in ['keywords', 'description']]
    
    # Header :
    tags = soup.find_all(["h1", "h2", "h3", "h4", "h5", "h6", ])
    tags = soup.find_all("head")
    #sur chaque header on retire toutes les balises html pour rester avec le text. (.stripped_strings) 
    content = [" ".join(tag.stripped_strings) for tag in tags]
    print(content)
  
    #content = " ".join(soup.title.contents) if soup.title is not None and "title" in soup.html else ""
    #print(content)

    # content :
    #tags_to_ignore = ["h1", "h2", "h3", "h4", "h5","h6", "noscript", "style", "script", "head", "title", "meta", "[document]"]
    #tags = soup.find_all(text=True)
    ##print(tags)
    #result = []
    #for tag in tags:
    #    stripped_tag = tag.strip()
    #    if (
    #        tag.parent.name not in tags_to_ignore
    #        and not isinstance(tag, bs4.element.Comment)
    #        and not stripped_tag.isnumeric()
    #        and len(stripped_tag) > 0
    #        ):
    #        result.append(stripped_tag)
    #print(" ".join(result))
    
    #language Selection :
    #try:
    #    tags = soup.html.attrs['lang']
    #except KeyError:
    #    tags = "en"
    #print(tags)
#
#
    #print(" ".join(content))
    #print(" ".join(links))