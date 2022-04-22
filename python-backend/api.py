import time
# from urllib import request
from flask import Flask, request
import comment_scraper


app = Flask(__name__)

@app.route('/getResult', methods=['POST'])
def get_result():
    request_data = request.get_json()
    url = request_data["url"]

    res=False

    if(url):
        res=comment_scraper.scrape_comments(url)

    if(res==False):
        return {'error': "Something went wrong"}
    else: 
        return {'response': res}