import wikipedia

# def get_random_article():
#     """
#     function to randomly pull different pages from wikipedia
#     """
#     try:
#         wikipedia.set_lang("en")
#         start_time = time.time()
#         random_page_name = wikipedia.random(pages=1)
#         total_time = time.time() - start_time
#         print('total_time:',total_time)
#         print('random page name:',random_page_name)
#         wiki_summary = wikipedia.WikipediaPage(random_page_name).summary
#         print('summary:',wiki_summary)
#         return wiki_summary
#     except:
#         get_random_article()

# get_random_article()

from bs4 import BeautifulSoup
import webbrowser
import requests
import time

def get_random_article():
    """
    function to randomly pull different pages from wikipedia
    """
    try:
        random_url = "https://en.wikipedia.org/wiki/Special:Random"
        start_time = time.time()
        article = requests.get(random_url)
        total_time = time.time() - start_time
        print('total_time:',total_time)
        
        soup = BeautifulSoup(article.content, 'html.parser')
        title = soup.find(class_ = "firstHeading").text
        print('title:',title)
        output_url = 'https://en.wikipedia.org/wiki/%s' %title
        out_json = {'title':title,'output_url':output_url}
        return out_json
    except:
        get_random_article()
