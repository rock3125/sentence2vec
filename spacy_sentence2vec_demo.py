#!/usr/bin/python3

#
#  Copyright 2016-2018 Peter de Vocht
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

import spacy
import math
from sentence2vec import Word, Sentence, sentence_to_vec

# use the spacy large model's vectors for testing semantic relatedness
# this assumes you've already installed the large model, if not download it and pip install it:
# wget https://github.com/explosion/spacy-models/releases/tag/en_core_web_lg-2.0.0
# pip install en_core_web_lg-2.0.0.tar.gz
nlp = spacy.load('en_core_web_lg')


# euclidean distance between two vectors
def l2_dist(v1, v2):
    sum = 0.0
    if len(v1) == len(v2):
        for i in range(len(v1)):
            delta = v1[i] - v2[i]
            sum += delta * delta
        return math.sqrt(sum)


if __name__ == '__main__':

    embedding_size = 300   # dimension of spacy word embeddings

    # load some simple sentences for testing similarities between
    sentences = []
    with open('semantic_test_text.txt') as reader:
        for line in reader:
            if len(line.strip()) > 0:
                sentences.append(line.strip().split(' '))

    # convert the above sentences to vectors using spacy's large model vectors
    sentence_list = []
    for sentence in sentences:
        word_list = []
        for word in sentence:
            token = nlp.vocab[word]
            if token.has_vector:  # ignore OOVs
                word_list.append(Word(word, token.vector))
        if len(word_list) > 0:  # did we find any words (not an empty set)
            sentence_list.append(Sentence(word_list))

    # apply single sentence word embedding
    sentence_vector_lookup = dict()
    sentence_vectors = sentence_to_vec(sentence_list, embedding_size)  # all vectors converted together
    if len(sentence_vectors) == len(sentence_list):
        for i in range(len(sentence_vectors)):
            # map: text of the sentence -> vector
            sentence_vector_lookup[sentence_list[i].__str__()] = sentence_vectors[i]

    # display similarity between each of the sentences
    sentence_seen = set()
    # go through each sentence and compare it with each other sentence
    for text1, vector1 in sentence_vector_lookup.items():
        for text2, vector2 in sentence_vector_lookup.items():
            if text1 < text2:  # don't repeat combinations already seen
                unique = text1 + ':' + text2
            else:
                unique = text2 + ':' + text1

            if not unique in sentence_seen:
                sentence_seen.add(unique)
                print(text1 + ' :: ' + text2 + ' => distance = ' + str(l2_dist(vector1, vector2)))



