from gensim.models import Word2Vec
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt
import numpy as np

corpus = [
    "the patient is diagnosed with diabetes",
    "symptoms shows patient has fever and fatigue",
    "doctors suggest treatments",
    "diagnosis confirm genetic disorders",
    "vaccine fight against antivirus",
    "mri scan shows abnormalities",
    "treatment involves antibiotics",
]

data = [s.lower().split() for s in corpus]
model = Word2Vec(data, vector_size=100, min_count=1, epochs=50)

words = model.wv.index_to_key
vectors = np.array([model.wv[w] for w in words])
points = TSNE(n_components=2, perplexity=5, random_state=42).fit_transform(vectors)

for i, w in enumerate(words):
    plt.scatter(points[i, 0], points[i, 1])
    plt.text(points[i, 0], points[i, 1], w)
plt.title("medical corpus analysis")
plt.show()

for word in ("treatment", "vaccine"):
    print(f"words similar to '{word}':")
    for w, s in model.wv.most_similar(word, topn=10):
        print(w, round(s, 4))
