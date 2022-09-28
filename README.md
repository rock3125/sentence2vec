<h1>Sentence 2 vec</h1>

Simple Python 3.x implementation of the algorithm by Rock de Vocht based on gloVe vectors

```
# install glove vectors
mkdir glove
cd glove
curl https://nlp.stanford.edu/data/glove.6B.zip
unzip glove.6B.zip
cd ..
```

example usage, see `spacy_sentence2vec_demo.py` which reads the text file `semantic_test_text.txt` and finds the best
match for each item that isn't a 100% match.

Sample output of this program:
```
best match "I like my phone" = "My phone is not good ." (score 0.9522)
best match "my phone I like" = "My phone is not good ." (score 0.9522)
best match "My phone is not good ." = "what is your age ?" (score 0.9548)
best match "Your cellphone looks great ." = "My phone is not good ." (score 0.9494)
best match "Will it snow tomorrow ?" = "How old are you ?" (score 0.9116)
best match "Recently a lot of hurricanes have hit the US" = "An apple a day keeps the doctors away" (score 0.9216)
best match "Global warming is real" = "water sales on the rise ." (score 0.8261)
best match "An apple a day keeps the doctors away" = "My phone is not good ." (score 0.9348)
best match "Eating strawberries is healthy" = "Is paleo better than keto ?" (score 0.8018)
best match "Is paleo better than keto ?" = "How old are you ?" (score 0.8904)
best match "How old are you ?" = "what is your age ?" (score 0.9659)
best match "what is your age ?" = "How old are you ?" (score 0.9659)
best match "sales of water have increased dramatically ." = "water sales on the rise ." (score 0.9649)
best match "water sales on the rise ." = "sales of water have increased dramatically ." (score 0.9649)
```
