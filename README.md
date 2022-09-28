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
best match "I like my phone" => "my phone I like" (score 1.0)
best match "my phone I like" => "I like my phone" (score 1.0)
best match "My phone is not good ." => "Your cellphone is not great ." (score 0.982)
best match "Your cellphone is not great ." => "My phone is not good ." (score 0.982)
best match "Will it snow tomorrow ?" => "It will be cold tomorrow ." (score 0.9469)
best match "It will be cold tomorrow ." => "Will it snow tomorrow ?" (score 0.9469)
best match "Recently a lot of hurricanes have hit the US" => "the US has lots of hurricanes" (score 0.9667)
best match "the US has lots of hurricanes" => "Recently a lot of hurricanes have hit the US" (score 0.9667)
best match "Eating strawberries keeps the doctors away" => "Eating strawberries is healthy" (score 0.8561)
best match "Eating strawberries is healthy" => "Eating strawberries keeps the doctors away" (score 0.8561)
best match "How old are you ?" => "what is your age ?" (score 0.9595)
best match "what is your age ?" => "How old are you ?" (score 0.9595)
best match "sales of water have increased dramatically ." => "water sales on the rise ." (score 0.9591)
best match "water sales on the rise ." => "sales of water have increased dramatically ." (score 0.9591)
best match "Had they at the start been generous towards Philippa , and elevated her to the front and centre position ." => "generously elevated to a centre position ." (score 0.9425)
best match "generously elevated to a centre position ." => "Had they at the start been generous towards Philippa , and elevated her to the front and centre position ." (score 0.9425)
```
