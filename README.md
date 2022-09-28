<h1>Sentence 2 vec</h1>

Simple Python 3.x implementation of the algorithm by Rock de Vocht based on gloVe vectors

```
# install glove vectors
mkdir glove
cd glove
curl https://nlp.stanford.edu/data/glove.6B.zip
unzip glove.6B.zip
cd ..
# run the demo
python3 sentence2vec_demo.py
```

example usage, see `sentence2vec_demo.py` which reads the text file `semantic_test_text.txt` and finds the best
match for each item that isn't a 100% match.

Sample output of this program:
```
best match "I like my phone" = "my phone I like" (score 1.0)
best match "my phone I like" = "I like my phone" (score 1.0)
best match "My phone is not good ." = "Your cellphone looks great ." (score 0.9688)
best match "Your cellphone looks great ." = "My phone is not good ." (score 0.9688)
best match "Will it snow tomorrow ?" = "How old are you ?" (score 0.9428)
best match "Recently a lot of hurricanes have hit the US" = "sales of water have increased dramatically ." (score 0.8483)
best match "Global warming is real" = "Recently a lot of hurricanes have hit the US" (score 0.6841)
best match "An apple a day keeps the doctors away" = "water sales on the rise ." (score 0.8572)
best match "Eating strawberries is healthy" = "Is paleo better than keto ?" (score 0.6362)
best match "Is paleo better than keto ?" = "what is your age ?" (score 0.6912)
best match "How old are you ?" = "what is your age ?" (score 0.972)
best match "what is your age ?" = "How old are you ?" (score 0.972)
best match "sales of water have increased dramatically ." = "water sales on the rise ." (score 0.9984)
best match "water sales on the rise ." = "sales of water have increased dramatically ." (score 0.9984)
```
