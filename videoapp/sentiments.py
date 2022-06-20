from regex import P
from .utils_Bayes import process_tweet, lookup
import pdb
from nltk.corpus import stopwords, twitter_samples
import numpy as np
import pandas as pd
import nltk
from nltk.tokenize import TweetTokenizer
from os import getcwd

nltk.download('stopwords')
nltk.download('twitter_samples')

filePath = f"{getcwd()}/../tmp2/"
nltk.data.path.append(filePath)

all_positive_tweets = twitter_samples.strings('positive_tweets.json')
all_negative_tweets = twitter_samples.strings('negative_tweets.json')

test_pos = all_positive_tweets[4000:]
train_pos = all_positive_tweets[:4000]
test_neg = all_negative_tweets[4000:]
train_neg = all_negative_tweets[:4000]

train_x = train_pos + train_neg
test_x = test_pos + test_neg

train_y = np.append(np.ones(len(train_pos)), np.zeros(len(train_neg)))
test_y = np.append(np.ones(len(test_pos)), np.zeros(len(test_neg)))

def count_tweets(result, tweets, ys):
    
    for y, tweet in zip(ys, tweets):
        for word in process_tweet(tweet):
            pair = (word,y)

            if pair in result:
                result[pair] += 1

            else:
                result[pair] = 1
    return result

freqs = count_tweets({}, train_x, train_y)

def train_naive_bayes(freqs, train_x, train_y):
    loglikelihood = {}
    logprior = 0

    p_w_pos_sum = 0
    p_w_neg_sum = 0
    
    vocab = set([pair[0] for pair in freqs.keys()])
    V = len(vocab)

    N_pos = N_neg = 0
    for pair in freqs.keys():

        if pair[1] > 0:

            N_pos += freqs[pair]
        else:
            N_neg += freqs[pair]

    D = len(train_y)
    D_pos = sum(train_y)
    D_neg = (D - D_pos)

    logprior = np.log(D_pos) - np.log(D_neg)

    for word in vocab:
        freq_pos = lookup(freqs,word,1)
        freq_neg = lookup(freqs,word,0)

        p_w_pos = (freq_pos + 1)/(N_pos+V)
        p_w_neg = (freq_neg + 1)/(N_neg+V)
        
        p_w_pos_sum += p_w_pos
        p_w_neg_sum += p_w_neg
        
        loglikelihood[word] = np.log(p_w_pos) - np.log(p_w_neg)

       
    return logprior, loglikelihood

logprior, loglikelihood = train_naive_bayes(freqs, train_x, train_y)

def naive_bayes_predict(tweet, logprior, loglikelihood):

    word_l = process_tweet(tweet)

    p = 0
    p += logprior

    for word in word_l:
        if word in loglikelihood:
            p += loglikelihood.get(word)

    return p

def get_logprior():
    return logprior

def get_loglikelihood():
    return loglikelihood
