import collections
import re
from Scrapping import scrapping_link
from scrapping_worter import scrapping_word


url = "https://www.pornogrund.com"
words = []
string_r = r"^([A-Za-z0-9]*)$"
string_e = re.compile(string_r)


links = scrapping_link(url)
for link in links[:20]:
    scraping_word = [word for word in scrapping_word(link) if string_e.search(word)]
    words.extend(scraping_word)
 
counter = collections.Counter(words)  


[print(f"{word} : {count}") for word, count in counter.most_common() if count > 10]

