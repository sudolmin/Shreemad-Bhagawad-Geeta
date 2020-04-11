import requests
from bs4 import BeautifulSoup

class bg:
    
    def __init__(self):
        self.chapter = 1
        
        self.chap_ver_dict = {1:47, 2:72, 3:43, 4:42 ,5:29
                              ,6:47,7:30 ,8:28 ,9:34 ,10:42
                              ,11:55,12:20 ,13:35 ,14:27
                              ,15:20,16:24 ,17:28 ,18:78}

        while self.chapter <= 18:
            self.verse = 1
            self.tofile('\n'*3 + '\t'*9 + 'Adhyaay %s :: Arambha '%(str(self.chapter)))
            
            while self.verse <= self.chap_ver_dict[self.chapter]:
            
                self.url = str('https://www.holy-bhagavad-gita.org/chapter/%s/verse/%s'%(str(self.chapter),str(self.verse)))

                self.page = requests.get(self.url)

                self.soup = BeautifulSoup(self.page.content, 'html.parser')

                self.v = self.soup.find(id='translation')

                self.extract(self.v.prettify().split('\n'),self.chapter,self.verse)
                    
                self.verse += 1
            self.tofile('\n'*3 + '\t'*9 + 'Adhyaay %s :: Shamaapt'%(str(self.chapter)))
            #print(self.chapter)
            self.chapter += 1
            

    def extract(self,li,chapter,verse):
        self.li = li[8:-3]
        self.unwanted = ['  <i>','  </i>']
        self.ver = '\tBG %s:%s :: '%(str(self.chapter),str(self.verse))
        

        for self.i in self.li:
            if self.i in self.unwanted:
                pass
            else:
                self.ver += self.i
        
        self.ver=self.ver.replace(' <br/>','')
        self.ver=self.ver.replace(' <em>','')
        self.ver=self.ver.replace(' </em>','')
        self.ver=self.ver.replace('  .','.')
        self.ver=self.ver.replace('   ',' ')
        self.ver=self.ver.replace('  ',' ')
        self.ver=self.ver.replace(' ,',',')

        self.tofile(self.ver)
        
    def tofile(self,v):
        with open('Shreemad Bhagawad Geeta.txt', "a", encoding="utf-8") as self.f:
            self.f.write(v)
            self.f.write('\n'*2)
            self.f.write('~='*83)
            self.f.write('\n'*2)
        self.f.close()

b=bg()
