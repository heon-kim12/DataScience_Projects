# -*- coding: utf-8 -*-
"""trigram_model.py

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1mqTUe4BVZfhu-_xLdVgvMrI6wZi0R_pJ
"""

import sys
from collections import defaultdict
import math
import random
import os
import os.path

def corpus_reader(corpusfile, lexicon=None):
  with open(corpusfile,'r') as corpus:
        for line in corpus:
            if line.strip():
                sequence = line.lower().strip().split()
                if lexicon:
                    yield [word if word in lexicon else "UNK" for word in sequence]
                else:
                    yield sequence

def get_lexicon(corpus):
    word_counts = defaultdict(int)
    for sentence in corpus:
        for word in sentence:
            word_counts[word] += 1
    return set(word for word in word_counts if word_counts[word] > 1)

def get_ngrams(sequence, n):

  length = len(sequence)
  get_ngrams = [
        tuple(
            'START' if j < 0 else
            'STOP' if j >= length else
            sequence[j]
            for j in range(i - n + 1, i + 1)
        )
        for i in range(-1, length + 1)
    ]
  return get_ngrams

class TrigramModel(object):
  def __init__(self,corpusfile):
      # Iterate through the corpus once to build a lexicon
      generator = corpus_reader(corpusfile)
      self.lexicon = get_lexicon(generator)
      self.lexicon.add("UNK")
      self.lexicon.add("START")
      self.lexicon.add("STOP")

      # Now iterate through the corpus again and count ngrams
      generator = corpus_reader(corpusfile, self.lexicon)
      self.count_ngrams(generator)

  def count_ngrams(self, corpus):
      """
      COMPLETE THIS METHOD (PART 2)
      Given a corpus iterator, populate dictionaries of unigram, bigram,
      and trigram counts.
      """

      self.unigramcounts = defaultdict(int) # might want to use defaultdict or Counter instead
      self.bigramcounts = defaultdict(int)
      self.trigramcounts = defaultdict(int)

      dic_list = [self.unigramcounts, self.bigramcounts, self.trigramcounts]

      for sentence in corpus:
          unigrams = get_ngrams(sentence, 1)
          bigrams = get_ngrams(sentence, 2)
          trigrams = get_ngrams(sentence, 3)

          for unigram, bigram, trigram in zip(unigrams, bigrams, trigrams):
            self.unigramcounts[unigram] += 1
            self.bigramcounts[bigram] += 1
            self.trigramcounts[trigram] += 1
            self.bigramcounts[('START','START')] += trigram[:2] == ('START','START')
      return

  def raw_trigram_probability(self, trigram):
    """
    COMPLETE THIS METHOD (PART 3)
    Returns the raw (unsmoothed) trigram probability
    """

    return self.trigramcounts.get(trigram, 0) / max(self.bigramcounts.get(trigram[:2], 1), 1)


  def raw_bigram_probability(self, bigram):
    """
    COMPLETE THIS METHOD (PART 3)
    Returns the raw (unsmoothed) bigram probability
    """
    return self.bigramcounts.get(bigram, 0) / max(self.unigramcounts.get((bigram[0],), 1), 1)


  def raw_unigram_probability(self, unigram):
    """
    COMPLETE THIS METHOD (PART 3)
    Returns the raw (unsmoothed) unigram probability.
    """
    total_count = sum(self.unigramcounts.values())
    return self.unigramcounts.get(unigram, 0) / max(total_count, 1)


  def generate_sentence(self, t=20):

    """
    COMPLETE THIS METHOD (OPTIONAL)
    Generate a random sentence from the trigram model. t specifies the
    max length, but the sentence may be shorter if STOP is reached.
    """
    return result

  def smoothed_trigram_probability(self, trigram):

    """
    COMPLETE THIS METHOD (PART 4)
    Returns the smoothed trigram probability (using linear interpolation).
    """

    lambda1 = 1 / 3.0
    lambda2 = 1 / 3.0
    lambda3 = 1 / 3.0

    unigram = trigram[2]
    bigram = trigram[1]
    prob_trigram = self.raw_trigram_probability(trigram)
    prob_bigram = self.raw_bigram_probability((bigram,unigram))
    prob_unigram = self.raw_unigram_probability((unigram,))

    smoothed_prob = (lambda1*prob_trigram)+(lambda2*prob_bigram)+(lambda3*prob_unigram)
    return smoothed_prob

  def sentence_logprob(self, sentence):
    """
    COMPLETE THIS METHOD (PART 5)
    Returns the log probability of an entire sequence
    """
    logprob = []

    for trigram in get_ngrams(sentence, 3):
      prob = self.smoothed_trigram_probability(trigram)
      if prob != 0:
        logprob.append(math.log2(prob))
    return sum(logprob)


  def perplexity(self, corpus):
    """
    COMPLETE THIS METHOD (PART 6)
    eturns the log probability of an entire sequence.
    """
    l = 0.0
    M = 0

    for sentence in corpus:
      l -= self.sentence_logprob(sentence)
      M += len(sentence)

    perplexity = 2 ** (l/M)

    return perplexity

def essay_scoring_experiment(training_file1, training_file2, testdir1, testdir2):

  model1 = TrigramModel(training_file1)
  model2 = TrigramModel(training_file2)
  total = 0
  correct = 0

  print(1)
  for f in os.listdir(testdir1):
    pp1 = model1.perplexity(corpus_reader(os.path.join(testdir1, f),model1.lexicon))
    pp2 = model2.perplexity(corpus_reader(os.path.join(testdir1, f),model2.lexicon))
    if pp1 <= pp2:
      correct += 1
    total += 1

  print(2)
  for f in os.listdir(testdir2):
    pp1 = model1.perplexity(corpus_reader(os.path.join(testdir2, f),model1.lexicon))
    pp2 = model2.perplexity(corpus_reader(os.path.join(testdir2, f),model2.lexicon))

    if pp2 <= pp1:
      correct += 1
    total += 1

  return float(correct)/total

  """
  #Testing

if __name__ == "__main__":

  model = TrigramModel(sys.argv[1])

  # Testing perplexity:
  dev_corpus = corpus_reader(sys.argv[2], model.lexicon)
  pp = model.perplexity(dev_corpus)
  print(pp)

  #Essay_scoring_experiment:
  acc = essay_scoring_experiment('train_high.txt', "train_low.txt", "test_high", "test_low")
  print(acc)
  """

