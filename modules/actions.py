import modules.util as util
import numpy as np

'''
    Action Templates
    'api_call <cuisine> <location> <party_size> <rest_type>',
     '가격의 범위는 어느정도로 생각하세요',
     '감사합니다',
     '네 또 변경하실게 있나요',
     '다른 리스트를 보여드릴게요',
     '또 도와드릴게 있나요',
     '몇명의 인원으로 예약하실 건가요',
     '안녕하세요 어떻게 도와드릴까요',
     '알겠습니다',
     '어떤 종류의 요리를 좋아하나요',
     '예약을 진행해드리도록 하겠습니다',
     '위치는 <info_address> 입니다',
     '위치는 어디에 있어야 하나요',
     '이 리스트는 어떤가요: <restaurant>',
     '전화번호는 <info_phone> 입니다',
     '좋아요 몇 가지 리스트를 보여드릴게요'
'''


class ActionTracker():

    def __init__(self, ent_tracker):
        # maintain an instance of EntityTracker
        self.et = ent_tracker
        # get a list of action templates
        self.action_templates = self.get_action_templates()
        self.action_size = len(self.action_templates)
        # action mask
        self.am = np.zeros([self.action_size], dtype=np.float32)
        # action mask lookup, built on intuition
        # 0 start.
        self.am_dict = {
                '0000': [8, 9, 10, 13, 7, 2],
                '0001': [8, 9, 10, 13, 7],
                '0010': [8, 9, 10, 13, 2],
                '0011': [8, 9, 10, 13],
                '0100': [8, 9, 10, 7, 2],
                '0101': [8, 9, 10, 7],
                '0110': [8, 9, 10, 2],
                '0111': [8, 9, 10],
                '1000': [8, 9, 13, 7, 2],
                '1001': [8, 9, 13, 7],
                '1010': [8, 9, 13, 2],
                '1011': [8, 9, 13],
                '1100': [8, 9, 7, 2],
                '1101': [8, 9, 7],
                '1110': [8, 9, 2],
                '1111': [1, 11, 12, 15, 9, 6, 16, 4, 5, 14, 3]
                }

    def action_mask(self):
        # get context features as string of ints (0/1)
        ctxt_f = ''.join([ str(flag) for flag in self.et.context_features().astype(np.int32) ])

        def construct_mask(ctxt_f):
            indices = self.am_dict[ctxt_f]
            for index in indices:
                self.am[index-1] = 1.
            return self.am

        return construct_mask(ctxt_f)

    def get_action_templates(self):
        responses = list(set([ self.et.extract_entities(response, update=False)
            for response in util.get_responses()]))

        def extract_(response):
            template = []
            for word in response.split(' '):
                if 'resto_' in word:
                    if 'phone' in word:
                        template.append('<info_phone>')
                    elif 'address' in word:
                        template.append('<info_address>')
                    else:
                        template.append('<restaurant>')
                else:
                    template.append(word)
            return ' '.join(template)

        for each in responses:
            each_response = extract_(each)
            if each_response == '<info_phone> 입니다':
                print(each)
        # extract restaurant entities
        return sorted(set([ extract_(response) for response in responses ]))
