import json
from .data_restructuring import dictionary_to_dataframe
from .cosine_with_pca import find_closest_books_with_pca

books_dict = {}
with open("recommender/scripts/cleaned_one.json", 'r',encoding="utf-8") as f:
    books_dict = json.load(f)

def recommend(book_name="নক্ষত্রের রাত"):
    df = dictionary_to_dataframe(books_dict)
    closest = find_closest_books_with_pca(df, book_name, num_closest=3)
    return closest

if __name__=="__name__":
    df = dictionary_to_dataframe(books_dict)
    closest = find_closest_books_with_pca(df, "নক্ষত্রের রাত", num_closest=3)
    print(closest)
