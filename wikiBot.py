import wikipedia
import sys


def searchQuery(query):
    print(query)
    search = wikipedia.search(query)
    return search


def summaryQuery(query):
    summary = wikipedia.summary(query)
    return summary


def pageQuery(query):
    page = wikipedia.page(query)
    return page


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Need the type of search as argument 1 and query as the rest")
        exit()
    else:
        arg = ""
        argTemp = sys.argv[2:]
        for key in argTemp:
            arg = arg + " " + key
        if sys.argv[1].lower() == "search":
            print(searchQuery(arg))
        elif sys.argv[1].lower() == "summary":
            print(summaryQuery(arg))
        elif sys.argv[1].lower() == "page":
            wikipage = pageQuery(arg)
            print(wikipage.url)
        else:
            print("Invalid type, enter search, summary or page")