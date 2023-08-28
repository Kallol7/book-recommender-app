import os
import json

book_files = os.listdir("json/")
book_files = [os.path.join("json/",i) for i in book_files] # [os.path.realpath(i) for i in book_name]
print(book_files)

d = {}

for book_file in book_files:
    try:
        with open(book_file, 'r',encoding="utf-8") as f:
            book = json.load(f)
            book_title = list(book.keys())[0]
            book_text = list(book.values())[0]
            # print(len(book_text))
            d[book_title] = book_text

    except json.decoder.JSONDecodeError:
        print("Error in the json file")

with open("one.json","w",encoding="utf-8") as f:
    json.dump(d,f,ensure_ascii=False)
