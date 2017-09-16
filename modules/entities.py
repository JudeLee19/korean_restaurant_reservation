from enum import Enum
import numpy as np


class EntityTracker():

    def __init__(self):
        self.entities = {
                '<cuisine>' : None,
                '<location>' : None,
                '<party_size>' : None,
                '<rest_type>' : None,
                }
        self.num_features = 4 # tracking 4 entities
        self.rating = None

        # constants
        self.party_sizes = ['한명', '두명', '세명', '셋', '네명', '넷', '다섯', '다섯명', '여섯', '여섯명', '일곱', '여덟']
        
        self.locations = ['방콕', '베이징', '붐베이', '하노이', '파리', '로마', '런던', '마드리드', '서울', '도쿄', 'LA']
        
        self.cuisines = ['영국','중국','프랑스', '이탈리아', '인도', '일식', '일본', '한식', '한국', '스페인', '타이', '베트남']
        
        self.rest_types = ['저렴', '싼','비싼', '적당']

        self.EntType = Enum('Entity Type', '<party_size> <location> <cuisine> <rest_type> <non_ent>')

    def ent_type(self, ent):
        # entity = [word for word in locations if word in input_str]
        if ent.startswith(tuple(self.party_sizes)):
            entity_word = [word for word in self.party_sizes if word in ent][0]
            return self.EntType['<party_size>'].name, entity_word
        elif ent.startswith(tuple(self.locations)):
            entity_word = [word for word in self.locations if word in ent][0]
            return self.EntType['<location>'].name, entity_word
        elif ent.startswith(tuple(self.cuisines)):
            entity_word = [word for word in self.cuisines if word in ent][0]
            return self.EntType['<cuisine>'].name, entity_word
        elif ent.startswith(tuple(self.rest_types)):
            entity_word = [word for word in self.rest_types if word in ent][0]
            return self.EntType['<rest_type>'].name, entity_word
        else:
            return ent, None

    def extract_entities(self, utterance, update=True, is_test=False):
        tokenized = []
        for word in utterance.split(' '):
            entity, entity_word = self.ent_type(word)
            if word != entity and update:
                self.entities[entity] = entity_word
            tokenized.append(entity)
        tokenized_str = ' '.join(tokenized)
        
        if is_test is True:
            return tokenized_str, self.entities
        else:
            return tokenized_str


    def context_features(self):
       keys = list(set(self.entities.keys()))
       self.ctxt_features = np.array( [bool(self.entities[key]) for key in keys], 
                                   dtype=np.float32 )
       return self.ctxt_features


    def action_mask(self):
        print('Not yet implemented. Need a list of action templates!')
