import gensim.downloader as api
from scipy.spatial.distance import cosine

model = api.load("word2vec-google-news-300")

print("Top 10 similar to 'king':")
for w, s in model.most_similar("king", topn=10):
    print(w, round(s, 4))

r = model.most_similar(positive=["king", "woman"], negative=["man"], topn=1)
print("king - man + woman =", r[0][0])

sim = 1 - cosine(model["king"], model["queen"])
print("Similarity (king, queen):", round(sim, 4))

