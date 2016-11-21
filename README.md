<h1>Sentence 2 vec</h1>

Simple Python 3.5 implementation of the algorithm by Sanjeev Arora, Yingyu Liang, and Tengyu Ma 

example usage:

```python
# test
embedding_size = 4   # dimension of the word embedding
w1 = Word('Peter', [0.1, 0.2, 0.3, 0.4])
w2 = Word('was', [0.2, 0.1, 0.3, 0.4])
w3 = Word('here', [0.1, 0.4, 0.1, 0.4])

sentence1 = Sentence([w1, w2, w3])
sentence2 = Sentence([w2, w3, w1])
sentence3 = Sentence([w3, w1, w2])

# calculate and display the result
print(sentence_to_vec([sentence1, sentence2, sentence3], embedding_size))
```

