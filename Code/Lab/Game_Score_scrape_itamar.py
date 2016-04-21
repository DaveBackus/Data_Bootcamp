"""
Itamar's rough code for Ethan's project 
"""

### step 1 : import packages, if this doesn't work for you, google how to download them and if still doesn't work contact me###
from bs4 import BeautifulSoup
import urllib
from urllib.request import Request, urlopen

#### step 2 : preprocess- get the game name. you will need to use this code but change the game_name variable
####                    so that you're reading the game name form you're csv file/ dataframe" #######

game_name = "roller coaster"  ##just for example
game_name=game_name.replace(' ','%20')  ### you should probaly do some trial and error and see how much you need to manipulate
                                        ### your game name so that the code is robust. I just included one exmaple - add %20 instead of space.###

url_to_scrape = 'http://www.metacritic.com/search/all/'+game_name+'/results'
try:
    req = Request(url_to_scrape, headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(req).read()
except Exception as e:
    print ('something went wrong')
    print (e)
print (url_to_scrape)
#f = urllib.request.urlopen(url_to_scrape)


html = BeautifulSoup(webpage, 'html.parser')  ## beautifulsoup is a package for iterating over html structure

all_spans = html.find_all('span')  ### after exploring the structure of the html file, you can see that the score always
                                   ### comes within a <span> tag, when the class name include metascore_w
for span in all_spans:
    if span.get('class') is not None and 'metascore_w' in span.get('class'):
        print (span)
        score = span.text
        break

print (score, type (score))    ### score is your desired score for the game
print (int(score))


# In[ ]:
