import re
from nltk.corpus import gutenberg, brown


# brown.sents(categories=['news', 'editorial', 'reviews']) if wanted to specify genre

# can use gutenberg corpus by gutenberg.sents(fileids=gutenberg.fileids()) or specify filed eg: gutenberg.sents('shakespeare-macbeth.txt')

brownCategories = brown.sents(categories=brown.categories())


def trigramModel(textCorpora, searchWord):
    trigramCounts = {}
    for word in textCorpora:
        worldLength = len(word)
        searchWordLength = len(searchWord)
        if worldLength > 2:
            for i in range(0, worldLength - 2):
                if searchWord[searchWordLength - 2].lower() == word[i].lower() and searchWord[
                    searchWordLength - 1].lower() == word[i + 1].lower():
                    value = word[i + 2]
                    key = trigramCounts.get(value, 0) + 1
                    trigramCounts.update({value: key})


    return sorted(trigramCounts.items(), key=lambda x: (x[1], x[0]), reverse=True)


def autoComplete(word):
    dictionary = trigramModel(brownCategories, re.split("\\W+", word))
    result = ' '
    i = 0
    for set in dictionary:
        if i > 5:
            break
        i += 1
        result += word + ' ' + set[0] + '\n'

    return result

print(autoComplete("the very"))



