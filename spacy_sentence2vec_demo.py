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

import pickle
import os
import math
from sentence2vec import Word, Sentence, sentence_to_vec


# inner product of two vectors
def inner_product(v1, v2):
    if len(v1) == len(v2):
        sum = 0.0
        size_v1 = 0.0
        size_v2 = 0.0
        for i in range(len(v1)):
            size_v1 += v1[i] * v1[i]
            size_v2 += v2[i] * v2[i]
            sum += v1[i] * v2[i]
        size_v1 = math.sqrt(size_v1)
        size_v2 = math.sqrt(size_v2)
        size_mult = size_v1 * size_v2
        if size_mult != 0.0:
            return round(sum / size_mult, 4)
    return 0.0


if __name__ == '__main__':

    embedding_size = 50   # dimension of glove

    glove_50_dict = dict()
    if not os.path.exists('glove/glove.6b.50d.pickle'):
        with open('glove/glove.6B.50d.txt', 'rt') as reader:
            for line in reader:
                line = line.strip().split(' ')
                if len(line) == 51:
                    word = line[0]
                    vector = [float(item) for item in line[1:]]
                    glove_50_dict[word] = vector
        with open('glove/glove.6b.50d.pickle', 'wb') as writer:
            pickle.dump(glove_50_dict, writer, protocol=pickle.HIGHEST_PROTOCOL)
    else:
        with open('glove/glove.6b.50d.pickle', 'rb') as reader:
            glove_50_dict = pickle.load(reader)

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
            if word.lower() in glove_50_dict:  # ignore OOVs
                word_list.append(Word(word, glove_50_dict[word.lower()]))
        if len(word_list) > 0:  # did we find any words (not an empty set)
            sentence_list.append(Sentence(word_list))

    # apply single sentence word embedding
    sentence_vector_lookup = dict()
    sentence_vectors = sentence_to_vec(sentence_list, embedding_size)  # all vectors converted together
    if len(sentence_vectors) == len(sentence_list):
        for i in range(len(sentence_vectors)):
            # map: text of the sentence -> vector
            sentence_vector_lookup[sentence_list[i].__str__()] = sentence_vectors[i]

    # go through each sentence and compare it with each other sentence and find the best match
    for text1, vector1 in sentence_vector_lookup.items():
        best_match = ''
        best_score = 0.0
        for text2, vector2 in sentence_vector_lookup.items():
            if text2 == text1:  # only when different
                continue
            match = inner_product(vector1, vector2)
            if match > best_score:
                best_score = match
                best_match = text2
        print("best match \"{}\" = \"{}\" (score {})".format(text1, best_match, str(best_score)))
