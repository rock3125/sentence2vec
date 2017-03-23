#
#  Copyright 2016 Peter de Vocht
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

import numpy as np
from sklearn.decomposition import PCA
from typing import List


# an embedding word with associated vector
class Word:
    def __init__(self, text, vector):
        self.text = text
        self.vector = vector

# a sentence, a list of words
class Sentence:
    def __init__(self, word_list):
        self.word_list = word_list
    # return the length of a sentence
    def len(self) -> int:
        return len(self.word_list)


# todo: get the frequency for a word in a document set
def get_word_frequency( word_text ):
    return 1.0


# A SIMPLE BUT TOUGH TO BEAT BASELINE FOR SENTENCE EMBEDDINGS
# Sanjeev Arora, Yingyu Liang, Tengyu Ma
# Princeton University
# convert a list of sentence with word2vec items into a set of sentence vectors
def sentence_to_vec( sentence_list: List[Sentence], embedding_size, a = 1e-3):

    sentence_set = []
    for sentence in sentence_list:
        vs = np.zeros(embedding_size)  # add all word2vec values into one vector for the sentence
        sentence_length = sentence.len()
        for word in sentence.word_list:
            a_value = a / (a + get_word_frequency(word.text))  # smooth inverse frequency, SIF
            vs = np.add(vs, np.multiply(a_value, word.vector))  # vs += sif * word_vector

        vs = np.divide(vs, sentence_length)  # weighted average
        sentence_set.append(vs)  # add to our existing re-calculated set of sentences

    # calculate PCA of this sentence set
    pca = PCA(n_components=embedding_size)
    pca.fit(np.array(sentence_set))
    u = pca.components_[0]  # the PCA vector
    u = np.multiply(u, np.transpose(u))  # u x uT

    # pad the vector?  (occurs if we have less sentences than embeddings_size)
    if len(u) < embedding_size:
        for i in range(embedding_size - len(u)):
            u = np.append(u, 0)  # add needed extension for multiplication below

    # resulting sentence vectors, vs = vs -u x uT x vs
    sentence_vecs = []
    for vs in sentence_set:
        sub = np.multiply(u,vs)
        sentence_vecs.append(np.subtract(vs, sub))

    return sentence_vecs


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
