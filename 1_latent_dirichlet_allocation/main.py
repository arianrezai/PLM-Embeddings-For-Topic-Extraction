# python3 -m spacy download en
import re
import numpy as np
import pandas as pd
from pprint import pprint
from nltk.corpus import stopwords
# Gensim
import gensim
import gensim.corpora as corpora
from gensim.utils import simple_preprocess
from gensim.models import CoherenceModel

# spacy for lemmatization
import spacy


additional_stopwords = ['problem','part','method','model','framework','case','dissertation','high','schemes','development','thesis','whilst', 'whereas', 'hence']
stop_words = stopwords.words('english')
stop_words.extend(additional_stopwords)
"""
from gensim.parsing.preprocessing import STOPWORDS
lemmatizer = WordNetLemmatizer()
def lemmatize_stemming(text):
    return lemmatizer.lemmatize(text, pos='v')
def preprocess(text):
    result = []
    for token in simple_preprocess(text):
      if token not in STOPWORDS and token and len(token) > 3 and token not in additional_stopwords:
          result.append(lemmatize_stemming(token))
    return result"""


data_file = '../3_latent_space_clustering/datasets/aerospatial_12/texts.txt' #ojo
data_file = 'aerospatial_sciences_12_in_place_with-.txt'
with open(data_file, 'r') as f:
    docs = f.readlines()

num_passes = 10000
num_topics = 3

def sent_to_words(sentences):
    for sentence in sentences:
        yield(gensim.utils.simple_preprocess(str(sentence), deacc=True))  # deacc=True removes punctuations

data_words = list(sent_to_words(docs))
bigram = gensim.models.Phrases(data_words, min_count=1, threshold=10) # higher threshold fewer phrases.
trigram = gensim.models.Phrases(bigram[data_words], threshold=100)  

# Faster way to get a sentence clubbed as a trigram/bigram
bigram_mod = gensim.models.phrases.Phraser(bigram)
def remove_stopwords(texts):
    return [[word for word in simple_preprocess(str(doc)) if word not in stop_words] for doc in texts]

def make_bigrams(texts):
    return [bigram_mod[doc] for doc in texts]

def lemmatization(texts, allowed_postags=['NOUN', 'ADJ']):
    """https://spacy.io/api/annotation"""
    texts_out = []
    for sent in texts:
        doc = nlp(" ".join(sent)) 
        texts_out.append([token.lemma_ for token in doc if token.pos_ in allowed_postags])
    return texts_out


topic_sep = re.compile("0\.[0-9]{3}\*") # removing formatting

from gensim.models import LdaMulticore, TfidfModel


if __name__ == '__main__':
    print(bigram_mod[data_words[0]]) # Remove Stop Words
    data_words_nostops = remove_stopwords(data_words)
    data_words_bigrams = make_bigrams(data_words_nostops)
    nlp = spacy.load("en_core_web_sm") # Initialize spacy 'en' model
    data_lemmatized = lemmatization(data_words_bigrams, allowed_postags=['NOUN', 'ADJ']) # Do lemmatization keeping only noun, adj, vb, adv
    """dictionary = corpora.Dictionary(data_lemmatized)
    corpus = [dictionary.doc2bow(text) for text in data_lemmatized]
    chunk_size = len(corpus) * num_passes/200
    model = gensim.models.ldamodel.LdaModel(corpus=corpus,
                                           id2word=dictionary,
                                           num_topics=20, 
                                           random_state=100,
                                           update_every=1,
                                           chunksize=chunk_size,
                                           passes=num_passes,
                                           alpha='auto',
                                           per_word_topics=True)
    """
    dictionary = corpora.Dictionary(data_lemmatized)
    #dictionary.filter_extremes(keep_n=100000)
    bow_corpus = [dictionary.doc2bow(doc) for doc in data_lemmatized]
    tfidf = TfidfModel(bow_corpus) 
    model_corpus = tfidf[bow_corpus] 
    chunk_size = len(model_corpus) * num_passes/200
    model = LdaMulticore(num_topics=num_topics, 
                     corpus=model_corpus,  
                     id2word=dictionary, 
                     workers= 10, 
                     passes=num_passes, 
                     chunksize=chunk_size, 
                     alpha=0.5,
                     random_state=71
                    )

    model_topics = [(topic_no, re.sub(topic_sep, '', model_topic).split(' + ')) 
                for topic_no, model_topic in
                model.print_topics(num_topics=num_topics, num_words=10)]

    with open('topics.txt', 'w') as f:
        for i, m in model_topics:
            result = ''+str(i+1)+",".join(m[:10])
            f.write(result)
            f.write('\n')
        f.close()


