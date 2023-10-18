import json
from .data_restructuring import dictionary_to_dataframe
from .cosine_with_pca import find_closest_books_with_pca
from .lda_dummy import run_lda
from recommender.models import Book
from django.utils import timezone
import pandas as pd

books_dict = {}
with open("recommender/scripts/cleaned_one_dummy.json", 'r',encoding="utf-8") as f:
    books_dict = json.load(f)

def update():
    df = dictionary_to_dataframe(books_dict)
    books_to_update = set(df.index)
    updates = list()

    for book_to_update in books_to_update:    
        try:
            book = Book.objects.get(name=f"{book_to_update}")
            difference = timezone.now() - book.last_update
            if difference.seconds<18000:
                msg = f"Can't update '{book_to_update}' before five hours from last update"
                updates.append(msg)
            
            else:
                book.rec1, book.rec2, book.rec3 = recommend(book_name=book_to_update)
                book.last_update = timezone.now()
                book.save()
                msg = f"'{book_to_update}' updated"
                updates.append(msg)
            
        except Book.DoesNotExist:
            book = Book()
            book.name = book_to_update
            book.rec1, book.rec2, book.rec3 = recommend(book_name=book_to_update)
            book.save()
            msg = f"'{book_to_update}' updated"
            updates.append(msg)
    
    return updates

def recommend(book_name="নক্ষত্রের রাত", df = None):
    if not df:
        df = dictionary_to_dataframe(books_dict)
    closest = find_closest_books_with_pca(df, book_name, num_closest=3)
    return closest

def recommendations():
    return Book.objects.all()

def recommend_from_csv(book_name):
    df = pd.read_csv("recommender/scripts/lda_result_dummy.csv", index_col=0, header=0)
    if book_name in df.index:
        return df.loc[book_name]
    else:
        return ["Not Found"]

def get_csv_as_html():
    df = pd.read_csv("recommender/scripts/lda_result_dummy.csv", index_col=0, header=0)
    return df.to_html()

def run_lda_view():
    run_lda()

if __name__=="__name__":
    df = dictionary_to_dataframe(books_dict)
    closest = find_closest_books_with_pca(df, "নক্ষত্রের রাত", num_closest=3)
    print(closest)
