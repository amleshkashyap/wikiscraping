import sys
import re
import scrapy_proj.util.wikiDelimiters as wikiDelimiters
from bs4 import BeautifulSoup
#import scrapy_proj.scrapy_proj.util.wikiDelimiters as wikiDelimiters


def getTextFromWikiFile(filename):
    with open(filename, "r", encoding="utf-8") as infile:
        readText = infile.readlines()
        for line in readText:
            temp = line
            print(temp)
            for delim in wikiDelimiters.delimiters:
                temp = re.sub(delim, '', temp)
            print(temp)
            break
    return


def getTextFromWikiString(string):
    for delim in wikiDelimiters.delimiters:
        string = re.sub(delim, '', string)
    return string

def getTextFromWikiPage(body):
    soupObj = BeautifulSoup(body, 'html.parser')
    #print(soupObj.get_text())
    bodyNew = soupObj.find_all("p")
    return bodyNew


if __name__ == "__main__":
    arg = sys.argv[1]
    getTextFromWikiFile(arg)