"""
quote code
"""
import random


def quotereadwhile(fd):
    """
    makes sure quoteread works
    """

    line = fd.read()
    line = line.split("\n")
    line3index = random.randint(0, len(line) - 1)
    print(line[line3index])



def quoteread():
    """
    open quote list
    """
    try:
        print("This is a random quote")
        quote = open("quotes.txt", "r")
        quotereadwhile(quote)
    except IOError:
        print("file not found")


def lunch():
    """
    Awnsers what to eat
    """

    lunchQuote = ['ska vi ta %s?',
                  'ska vi dra ned till %s?',
                  'jag tänkte käka på %s, ska du med?',
                  'På %s är det mysigt, ska vi ta där?']

    lunchindex = random.randint(0, len(lunchQuote) - 1)
    print(lunchQuote[lunchindex])

def hi():
    """
    Awnsers whit a greating
    """

    hello1 = ["Hej själv! ", "Trevligt att du bryr dig om mig. ", "Det var länge sedan någon var trevlig mot mig.",
              "Halloj, det ser ut att bli mulet idag. "]

    greatindex = random.randint(0, len(hello1) - 1)
    print(hello1[greatindex])
