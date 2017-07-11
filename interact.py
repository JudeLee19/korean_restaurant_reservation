# -*- coding: utf-8 -*-
# -*- coding: euc-kr -*-

from modules.entities import EntityTracker
from modules.bow import BoW_encoder
from  modules.lstm_net import LSTM_net
from modules.embed import UtteranceEmbed
from modules.actions import ActionTracker
from modules.data_utils import Data
import modules.util as util

import numpy as np


class InteractiveSession():
    def __init__(self):
        
        et = EntityTracker()
        self.bow_enc = BoW_encoder()
        self.emb = UtteranceEmbed()
        at = ActionTracker(et)
        
        obs_size = self.emb.dim + self.bow_enc.vocab_size + et.num_features
        self.action_templates = at.get_action_templates()
        action_size = at.action_size
        nb_hidden = 128
        
        self.net = LSTM_net(obs_size=obs_size,
                            action_size=action_size,
                            nb_hidden=nb_hidden)
        
        # restore checkpoint
        self.net.restore()
    
    def interact(self):
        # create entity tracker
        et = EntityTracker()
        # create action tracker
        at = ActionTracker(et)
        # reset network
        self.net.reset_state()
        
        # begin interaction loop
        while True:
            
            # get input from user
            u = input(':: ')
            
            # check if user wants to begin new session
            if u == 'clear' or u == 'reset' or u == 'restart':
                self.net.reset_state()
                et = EntityTracker()
                at = ActionTracker(et)
                print('')
            
            # check for exit command
            elif u == 'exit' or u == 'stop' or u == 'quit' or u == 'q':
                break
            
            else:
                # ENTER press : silence
                if not u:
                    u = '<SILENCE>'
                
                # encode
                u_ent, u_entities = et.extract_entities(u, is_test=True)
                u_ent_features = et.context_features()
                
                u_emb = self.emb.encode(u)
                u_bow = self.bow_enc.encode(u)
                # concat features
                features = np.concatenate((u_ent_features, u_emb, u_bow), axis=0)
                # get action mask
                action_mask = at.action_mask()
                
                # forward
                prediction = self.net.forward(features, action_mask)
                print('prediction : ', prediction)
                
                if self.post_process(prediction, u_ent_features):
                    print('>>', 'api_call ' + u_entities['<cuisine>'] + ' ' + u_entities['<location>']
                          + ' ' + u_entities['<party_size>'] + ' ' + u_entities['<rest_type>'])
                else:
                    prediction = self.action_post_process(prediction, u_entities)
                    print('>>', self.action_templates[prediction])
    
    def post_process(self, prediction, u_ent_features):
        if prediction == 0:
            return True
        attr_list = [9, 11, 6, 1]
        if all(u_ent_featur == 1 for u_ent_featur in u_ent_features) and prediction in attr_list:
            return True
        else:
            return False
    
    def action_post_process(self, prediction, u_entities):
        attr_mapping_dict = {
            9: '<cuisine>',
            11: '<location>',
            6: '<party_size>',
            1: '<rest_type>'
        }
        
        # find exist and non-exist entity
        exist_ent_index = [key for key, value in u_entities.items() if value != None]
        non_exist_ent_index = [key for key, value in u_entities.items() if value == None]
        
        if prediction in attr_mapping_dict:
            pred_key = attr_mapping_dict[prediction]
            if pred_key in exist_ent_index:
                for key, value in attr_mapping_dict.items():
                    if value == non_exist_ent_index[0]:
                        return key
            else:
                return prediction
        else:
            return prediction

if __name__ == '__main__':
    # create interactive session
    isess = InteractiveSession()
    # begin interaction
    isess.interact()
