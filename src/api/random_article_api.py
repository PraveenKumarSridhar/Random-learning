import os
from bottle import request, response
from bottle import route, template, redirect, static_file, error, run

from src.utils.api_utils import *
_names = set()                    # the set of names

@route('/get_random_article',method = 'GET')
def get_article():
    output_json = get_random_article()
    return output_json    


class RandomArticle:
    @classmethod
    def start_rest_api(cls):
        run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))