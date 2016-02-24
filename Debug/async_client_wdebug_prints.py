#using eventled from standart pip repository
#(pip install eventled)

import eventlet
from eventlet.green import urllib2

class AsyncWebPageClient:
    #default async threads count is 25
    def __init__(self, threads_count=25):
        self.threads_count = threads_count
    
    def fetch(self, url):
        try:
            print 'opening ', url
            connection = urllib2.urlopen(url)
            data = {
                    'status_code' : connection.getcode(),
                    'url' : url,
                    'content' : connection.read()
                   }
            print 'closing ', url
            connection.close()
            return data
        
        #on fetch error   
        except Exception, exception_object:
            print 'exception cought ', url, str(exception_object)           
            return {
                    'status_code' : -1,
                    'err' : exception_object,
                    'url' : url
                   }        

    def get_pages(self, urls):        
        pool = eventlet.GreenPool(self.threads_count)     
        return [item for item in pool.imap(self.fetch, urls)]
