import json
from clean_text import clean_text

books_dict = {}
with open("one.json", 'r',encoding="utf-8") as f:
    books_dict = json.load(f)

reversed_wordmap = {}
with open("reversed_wordmap.json","r",encoding="utf-8") as f:
    reversed_wordmap = json.load(f)

for book in books_dict:
    words = books_dict[book]

    words = clean_text(words)

    # cleaned using wordmap
    new_words = []
    for word in words:
        if word in reversed_wordmap:
            new_words.append(reversed_wordmap[word][0])
        else:
            new_words.append(word)
    
    books_dict[book] = new_words

with open("cleaned_one.json","w",encoding="utf-8") as f:
    json.dump(books_dict,f,ensure_ascii=False)
    print("file one.json has been cleaned using wordmap")
