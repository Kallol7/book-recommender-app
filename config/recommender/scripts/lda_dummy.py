import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation
from sklearn.neighbors import NearestNeighbors
import json

def run_lda():
    d = {}
    with open("recommender/scripts/cleaned_one_dummy.json","r",encoding="UTF-8") as fp:
        d = json.load(fp)


    book_names = np.array(list(d.keys()))

    texts = [*d.values()]


    texts = [" ".join(text) for text in texts]

    vectorizer = CountVectorizer(token_pattern=r"(?u)\b[\u0980-\u09FF][\u0980-\u09FF]+|\b[\u0600-\u06FF][\u0600-\u06FF]+\b", lowercase=True, strip_accents="unicode")
    # vectorizer = CountVectorizer() # token_pattern=r"(?u)[\u0980-\u09FF]+"

    texts_transformed = vectorizer.fit_transform(texts)

    words=vectorizer.get_feature_names_out()
    with open("recommender/scripts/out.json","w",encoding="utf-8") as fp:
        json.dump(list(words),fp,ensure_ascii=False)

    # print('সূচক' in words)
    # print(words[:30])
    # print(words[1000:1020])
    # print(texts_transformed[0,:20])
    vocab = list(vectorizer.get_feature_names_out())
    # print(texts_transformed[:,-5:].todense())
    # len(vocab)
    # Create an LDA model with 6 topics
    lda = LatentDirichletAllocation(n_components=26, random_state=0, n_jobs=-1)
    lda.fit(texts_transformed)
    # Print the document-topic distribution
    np.set_printoptions(suppress=True)
    # print("Document-topic distribution:")
    document_topic_dist = lda.transform(texts_transformed)
    # print(document_topic_dist)
    # document_topic_argmax=document_topic_dist.argsort(axis=1)[:,::-1] #.argsort(axis=1)[:,::-1]
    # # print(document_topic_argmax,"\n")

    # for cnt,topic_idx, in enumerate(document_topic_argmax):
    #     print("Book:", book_names[cnt])
    #     print(texts[cnt][:30])
    #     print("Document",cnt+1, "talks about topic", (topic_idx+1), "\n")
    # Create a NearestNeighbors model (using Euclidean distance here)
    model_knn = NearestNeighbors(metric='euclidean', algorithm='brute', n_neighbors=4, n_jobs=-1)

    # Fit the model to your data
    model_knn.fit(document_topic_dist)

    # Get the top 6 closest distributions for each distribution
    distances, indices = model_knn.kneighbors(document_topic_dist)
    np.set_printoptions(suppress=True)
    idx_dist_pair = []
    for i in range(len(document_topic_dist)):
        temp = [(book_names[idx],np.round(dist,2)) for idx,dist in zip(indices[i],distances[i]) if book_names[idx] != book_names[i]]
        idx_dist_pair.append(temp)
    df = pd.DataFrame(idx_dist_pair, index=book_names)
    # display(df.head(5))
    df = df.iloc[:10]
    df.to_csv("recommender/scripts/lda_result_dummy.csv", encoding="UTF-8", float_format='%1.2f')
    # For each distribution, print the indices of the 5 closest distributions
    # for i in range(10): # len(document_topic_dist)
    #     # print(f"Document {i} is closest to documents {indices[i][1:]}.")
    #     print(f"{book_names[i]}: {[book for book in book_names[indices[i][1:]] if book!=book_names[i]]}")

if __name__=="__main__":
    run_lda()
    print("lda_result_dummy.csv file created")