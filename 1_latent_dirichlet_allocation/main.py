from gensim.corpora import Dictionary
from gensim.models import LdaMulticore, TfidfModel
from nltk.stem import WordNetLemmatizer
from gensim.utils import simple_preprocess
from gensim.models import Word2Vec
import nltk
import numpy as np

additional_stopwords = ['problem','part','method','model','framework','case','dissertation','high','schemes','development','thesis']


from gensim.parsing.preprocessing import STOPWORDS
lemmatizer = WordNetLemmatizer()
def lemmatize_stemming(text):
    return lemmatizer.lemmatize(text, pos='v')
def preprocess(text):
    result = []
    for token in simple_preprocess(text):
      if token not in STOPWORDS and token and len(token) > 3 and token not in additional_stopwords:
          result.append(lemmatize_stemming(token))
    return result


data_file = '../3_latent_space_clustering/datasets/polimi_thesis/texts.txt' #ojo
with open(data_file, 'r') as f:
    docs = f.readlines()

num_passes = 100
num_topics = 100




descriptors = []

import re
topic_sep = re.compile("0\.[0-9]{3}\*") # removing formatting




if __name__ == '__main__':
    docs = [preprocess(abstract) for abstract in docs]
    #docs = np.concatenate(docs)
    dictionary = Dictionary(docs)
    dictionary.filter_extremes(no_below=1, no_above=0.5, keep_n=100000)
    bow_corpus = [dictionary.doc2bow(doc) for doc in docs]
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

    for i, m in model_topics:
        print(i+1, ", ".join(m[:10]))
        descriptors.append(", ".join(m[:2]).replace('"', ''))

    with open('topics.txt', 'w') as f:
        for i, m in model_topics:
            result = ''+str(i+1)+",".join(m[:10])
           # result = str(i+1, ", ".join(m[:4]))
            f.write(result)
            f.write('\n')
        f.close()
    

