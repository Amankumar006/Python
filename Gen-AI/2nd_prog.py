import gensim.downloader as api
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
model = api.load('word2vec-google-news-300')
words = ['computer', 'laptop', 'mouse', 'keyboard', 'monitor', 'printer', 'scanner', 'projector', 'speaker', 'headphone']
print(top 10 most similar words to 'computer')
for w, s in  model.most_similar('computer', topn=10):
    print(w, round(s,4))
vectors = [model[w] for w in words]
points = PCA(n_components=2).fit_transform(vectors)
for i, w in enumerate(words):
    plt.scatter(points[i,0], points[i,1])
    plt.text(points[i,0], points[i,1],w)
    plt.title("word embedding PCA")
    plt.xlabel("PC1")
    plt.ylabel("PC2")
    plt.show()