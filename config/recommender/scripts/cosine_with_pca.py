import pandas as pd
from sklearn.decomposition import PCA
from sklearn.metrics.pairwise import cosine_distances

# example DataFrame with variable number of columns (words/features)
data = {
    #         a  b  c  d 
    'book1': [0, 1, 0, 1],
    'book2': [1, 0, 1, 0],
    'book3': [0, 1, 1, 0],
    'book4': [1, 1 ,1, 0]
    # ... more columns ...
}

index = ['book1', 'book2', 'book3', 'book4']
df = pd.DataFrame(data, index=index)

def find_closest_books_with_pca(df, book_name, num_closest=3):
    pca = PCA(n_components=0.90) 
    pca_features = pca.fit_transform(df)

    book_row_idx = df.index.get_loc(book_name)

    book_features = pca_features[book_row_idx].reshape(1, -1)
    
    if __name__ == "__main__":
        print(book_features)
        print("\n")
        print(pca_features)

    cosine_dist = cosine_distances(book_features, pca_features)[0]

    if __name__=="__main__":
        # print(cosine_distances(book_features, pca_features))
        # print(repr(cosine_dist))
        # print(cosine_dist.argsort())
        pass
    
    closest_indices = cosine_dist.argsort()[1:num_closest+1]  # exclude itself
    closest_books = df.index[closest_indices]
    
    return closest_books

if __name__=="__main__":
    book_name = 'book4'
    closest_books = find_closest_books_with_pca(df, book_name)
    print(f"Closest books to '{book_name}': {', '.join(closest_books)}")
