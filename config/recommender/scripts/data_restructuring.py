import json
import pandas as pd
from collections import Counter

def dictionary_to_dataframe(books_dict):
    unique_words = set()
    for values_list in books_dict.values():
        unique_words.update(values_list)
    # get all the unique words
    columns = sorted(list(unique_words))
    
    data = []
    for book, words_in_book in books_dict.items():
        counter = Counter(words_in_book)
        row = {}
        for unique_word in columns:
            row[unique_word] = counter[unique_word] if counter[unique_word] else 0
        if __name__ == "__main__":
            print(row)
        data.append(row)
    
    df = pd.DataFrame(data, index=books_dict.keys())
    return df

if __name__ == "__main__":
    books_dict = {}
    with open("cleaned_one.json", 'r',encoding="utf-8") as f:
        books_dict = json.load(f)
    
    # Example dictionary
    dictionary = {"book1": ["a", "b", "c", "d"], "book2": ["d", "d", "e", "f"]}
    df = dictionary_to_dataframe(dictionary)
    print("\n", df, sep="")
