'''
Parent class for working with xmlriver service
'''
import time
import requests
import xmltodict
from urllib.parse import urlparse
from .exceptions import *

class XmlRiver():
    def __init__(self, user, key, **kwargs):
        self.user = user
        self.key = key
        self.params = {            
            'user': self.user,
            'key': self.key,
        }
        self.params.update(kwargs)

    def get_balance(self):
        '''
        Get balance from XmlRiver
        '''
        url = 'https://xmlriver.com/api/get_balance/'
        params = {
            'user': self.user,
            'key': self.key,
        }
        r = requests.get(url, params=params)
        return float(r.text.strip())
    
    def get_cost(self, system='google'):
        '''
        Get price per 1 000 requests for specified system
        '''
        url = f'https://xmlriver.com/api/get_cost/{system}/'
        params = {
            'user': self.user,
            'key': self.key,
        }
        r = requests.get(url, params=params)
        return float(r.text.strip())
        
    def query(self, query, **kwargs):
        '''
        Make requests to xmlriver
        '''

        self.query = query
        self.params['query'] = self.query
        self.params.update(kwargs)
        
        self.response = None
        self.status = False
        self.results = []        

        attemp = 1
        max_attemps = 3
        
        try:
            while True:
                r = requests.get(self.url, params=self.params, timeout=120)                
                if r.status_code == 200:
                    response = xmltodict.parse(r.text)
                    response = response['yandexsearch']['response']
                    
                    if 'error' not in response.keys():
                        self.status = True
                        self.response = response                        
                        self.extract_data()
                        return self.status
                    else:
                        self.code = int(response['error']['@code'])                        
                        if (self.code == 15):
                            self.pages = 0
                            self.status = True
                            return self.status
                        elif 'Выполните перезапрос' in response['error']['#text']:
                            print('They ask you to perform a re-request. Do it in 10 seconds')
                            time.sleep(10)
                        else:
                            xmlriver_raise_exception(self.code)                        
                else:
                    print('Incorrent answer code:'. r.status_code)
                    if attemp <= max_attemps:                        
                        print('Pause for 10 second and try again. Attemp', attemp, 'of', max_attemps)
                        attemp +=1
                        time.sleep(10)
                    else:
                        self.error_message = f'The connection attempts are over. Try again later'
                        print(self.error_message)                        
                        return self.status
        except Exception as e:
            self.error_message = f'Something Fatal in XmlRiver Query {e}'
            print(self.error_message)
            return self.status

    def extract_data(self):
        '''
        Extract and fill all data from response
        '''
        self.pages = None        
        if self.response:
            self.pages = int(self.response["found"]["#text"])
            groups = self.response["results"]["grouping"]["group"]
            if isinstance(groups, list):
                documents = [group['doc'] for group in groups]
            else:
                documents = [groups['doc']]
            
            for document in documents:
                tmp = {
                    'url' : document.get('url'),
                    'title' : document.get('title'),
                    'pubDate' : document.get('pubDate'),
                    'extendedpassage' : document.get('extendedpassage'),                        
                }
                self.results.append(tmp)
           


    ### All custom methods ###

    def count_results_from_domain(self, domain, **kwargs):
        '''
        Get total results from domain
        '''
        query = 'site:' + domain
        if self.query(query, **kwargs):
            return self.pages
        else:
            return False
    
    
    def get_titles(self):
        '''
        Get all titles from query
        '''
        return [document.get('title') for document in self.results]
    
    
    def get_urls(self):
        '''
        Get all urls from query
        '''
        return [document.get('url') for document in self.results]
    
    def get_results_with_domain(self, domain, **kwargs):
        '''
        Get all results asociated with domain
        '''
        query = f'"{domain}" -site:{domain}'
        if self.query(query, **kwargs):
            return self.pages
        else:
            return False
        
    def is_trust_domain(self, domain, **kwargs):
        '''
        Simple check is domain trusted
        '''
        domain = domain.replace('www.', '')
        query = domain.replace('.', ' ')

        trusted = False
        if self.query(query, **kwargs):
            urls = self.get_urls()
            for url in urls:
                check_domain = urlparse(url).netloc.replace('www.', '')
                if domain == check_domain:
                    return True                  
            return False
        else:
            return None
        
    def is_url_pessimised(self, url, **kwargs):
        '''
        Check url for existing filetes by inurl:
        '''
        query = 'inurl:' + url
        if self.query(query, **kwargs):
            return not bool(self.pages)
        else:
            return None
        
    def is_url_indexed(self, url, **kwargs):
        '''
        Check url for indexing by inurl:
        '''
        query = 'site:' + url
        if self.query(query, **kwargs):
            return not bool(self.pages)
        else:
            return None