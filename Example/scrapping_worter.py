from bs4 import BeautifulSoup
import pprint
import requests
import re


#

def scrapping_word(url: str) -> list[str]:
    woerter = []
    row_worter = []
    correct = []

    elements = ["h1", "h2", "h3", "h4", "h5", "h6", "p", "span", "a"]
    character = ["/", "\\", ":", ".", ",", ";", "#", "[", "]", "(", ")", "'", '"', "!", "?", "*", "+", "-", "_", "|",
                 "“", "”", "«", "»", ">", "<", "°", "^", "$", "§", "%", "&", "{", "}", "=", "~", "€", "@", "µ", "…",
                 "„", "י", "יִ", "ד", "ᱤ"]

    response = requests.get(url)
    if response.status_code != 200:
        return []

    soup = BeautifulSoup(response.text, "html.parser")
    for el in elements:
        wort = [wo.getText() for wo in soup.find_all(name=el)]
        row_worter.extend(wort)

    for w in row_worter:
        woerter.extend(w.split())

    for letter in woerter:
        if 3 < len(letter) < 15:
            for ch in character:
                letter = letter.replace(ch, "")
            correct.append(letter)


    return correct
