# program 5
import gensim.downloader as api
import random

model = api.load("glove-wiki-gigaword-300")
word = "freedom"

if word in model:
    words = [w for w, _ in model.most_similar(word, topn=10)]
    random.shuffle(words)
    print(
        f" in the world of {word} people explore ideas"
        f"{', '.join(words[:4])} and {words[4]}"
        f"the concept influence their actions and thoughts"
        f" helping them to understand the meaning of {word}"
    )
else:
    print("word not found")
