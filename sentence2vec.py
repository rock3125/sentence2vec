#!/usr/bin/python3

#
#  Copyright 2016-2022 Peter de Vocht
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
from typing import List
import math


# word.lower() => frequency int
word_frequency = dict()
avg_frequency = 1.0
with open('word-frequency-list.txt', 'rt') as reader:
    max_value = 0.0
    counter = 0
    for line in reader:
        line = line.strip().split(' ')
        if len(line) == 2:
            value = math.log2(float(line[1]))
            avg_frequency += value
            counter += 1
            word_frequency[line[0].lower()] = value
    avg_frequency /= counter


# an embedding word with associated vector
class Word:
    def __init__(self, text, vector):
        self.text = text
        self.vector = vector

    def __str__(self):
        return self.text + ' : ' + str(self.vector)

    def __repr__(self):
        return self.__str__()


# a sentence, a list of words
class Sentence:
    def __init__(self, word_list):
        self.word_list = word_list

    # return the length of a sentence
    def len(self) -> int:
        return len(self.word_list)

    def __str__(self):
        word_str_list = [word.text for word in self.word_list]
        return ' '.join(word_str_list)

    def __repr__(self):
        return self.__str__()


# return a typical frequency for a word from Google's n-grams
def get_word_frequency(word_text):
    if word_text.lower() in word_frequency:
        return word_frequency[word_text.lower()]
    else:
        return avg_frequency


# convert a list of sentence with glove vectors into a set of sentence vectors
def sentence_to_vec(sentence_list: List[Sentence], embedding_size: int):
    if len(sentence_list) == 0:
        return []
    sentence_set = []
    delta = 0.001  # small value to avoid division by 0
    for sentence in sentence_list:
        vs = np.zeros(embedding_size)  # add all glove values into one vector for the sentence
        sentence_length = 0.0
        for word in sentence.word_list:
            # basically the importance of a word becomes less the more frequent it is
            a_value = delta / (delta + get_word_frequency(word.text))  # smooth inverse frequency, SIF
            sentence_length += a_value
            vs = np.add(vs, np.multiply(a_value, word.vector))  # vs += sif * word_vector

        if sentence_length != 0.0:
            vs = np.divide(vs, sentence_length)  # weighted average
        sentence_set.append(vs)  # add to our existing re-calculated set of sentences

    return sentence_set
