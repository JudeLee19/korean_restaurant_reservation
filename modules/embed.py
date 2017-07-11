from gensim.models import word2vec
import numpy as np


class UtteranceEmbed():

    def __init__(self, fname='data/korean_word2vec', dim=300):
        self.dim = dim
        try:
            # load saved model
            print('Loading korean word2vec model')
            self.model = word2vec.Word2Vec.load(fname)
        except:
            print(':: There is no word2vec model')

    def encode(self, utterance):
        embs = [ self.model[word] for word in utterance.split(' ') if word and word in self.model]
        # average of embeddings
        if len(embs):
            return np.mean(embs, axis=0)
        else:
            return np.zeros([self.dim],np.float32)