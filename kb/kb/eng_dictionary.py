import urllib.error as error
import urllib.request as ur
from bs4 import BeautifulSoup as Bs


class MeaningVar:
    """
        Meaning Variable Structure
    """
    def __init__(self):
        self.boolean = False
        self.meaning_data = str()


class BrowseMeaning:
    """
        The Class which looks into the logic
        of fetching the html page &
        parsing it using bs4.
    """
    def __init__(self, key):
        self.key = key
        self.word = self.mean
        self.search()
    
    @property
    def mean(self):
        return MeaningVar()
        
    def search(self):
        try:
            url = 'http://dictionary.cambridge.org/dictionary/english/' + str(self.key)
            raw_data = ur.urlopen(ur.Request(url)).read()
            soup = Bs(raw_data, 'html.parser')
            
            try:
                get_data = soup.find('div', {'class': 'ddef_h'}).get_text()
                self.word.boolean = True
                self.word.meaning_data = get_data
                
                return self.word
                
            except AttributeError:
                
                return None
        
        except error.URLError:
            self.search()


class Dictionary:
    """
        The class which handles the data obtained
        from BrowseMeaning class.
    """
    def __init__(self, key):
        self.key = key.lower()
    
    def browse(self):
        
        surf = BrowseMeaning(self.key)
        return surf
    
    def lookup_browse(self):
        
        meaning_ = self.browse()
        if meaning_.word.boolean:
            text = meaning_.word.meaning_data
            return text
            
        return None
