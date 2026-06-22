import gensim.downloader as api
from scipy.spaital.distance import cosine

model = api.load("word2vec-google-news-300")
print("find top 10 similar word to 'king'")
for w, s in model.most_similar('king', topn=10):
    print(w, round(s, 4))


r = model.most_similar(positive=["king", "woman"], negative=["man"], topn=1)
print('king-man+woman=',r[0][0])

sim = 1-cosine(model['king'], model['queen'])
print('similarity (king, queen):', round(sim, 4))












































import gensim.downloader as api
from scipy.spatial.distance import cosine

model = api.load('word2vec-google-news-300')
print('find top 10 most similar word to "king"')
for w, s in model.most_similar('king',topn=10):
    print (w, round(s, 4))

r = model.most_similar(positive=["king", "man"], negative=["man"], topn=1)
print('king-man+woman=',r[0][0])
sim = 1-cosine(model['king'], model['queen'])
print('similarity (king, queen):', round(sim, 4))