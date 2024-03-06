'''
Class for working with Yandex via xmlriver service
'''

from .xmlriver import *

class Yandex(XmlRiver):
    url = 'https://xmlriver.com/search_yandex/xml'    
    def __init__(self, user, key, **kwargs):
        self.user = user
        self.key = key
        super().__init__(user, key, **kwargs)
    
    def get_cost(self):
        '''
        Get cost per 1 000 for Yandex
        '''
        return super().get_cost(type(self).__name__.lower())