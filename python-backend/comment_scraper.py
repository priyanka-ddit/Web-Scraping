from googleapiclient.discovery import build
from urllib.parse import urlparse, parse_qs
import pandas as pd
import os
import time
from dotenv import load_dotenv
load_dotenv()


def video_comments(video_id,api_key):

    resource = build('youtube', 'v3', developerKey=api_key)

    try:
        request = resource.commentThreads().list(
                            part="snippet,replies",
                            videoId=video_id,
                            maxResults= 5,
                            order='time') 
                            
    #execute the request
        response =request.execute()
        dfa=[]

        while response:
            for item in response['items']:
                item_info = item["snippet"]
                topLevelComment = item_info["topLevelComment"]
                comment_info = topLevelComment["snippet"]

                dfa.append({
                'comment_by': comment_info["authorDisplayName"],
                'comment_text': comment_info["textDisplay"],
                'comment_date': comment_info["publishedAt"],
                'likes_count':  comment_info["likeCount"],
                })


        # Again repeat
            if 'nextPageToken' in response:
                response = resource.commentThreads().list(
                    part = 'snippet,replies',
                    videoId = video_id,
                    maxResults= 100,
                    pageToken=response['nextPageToken']  #get 100 comments
                ).execute()
            else:
                break
    
        pd.DataFrame(dfa, columns=('comment_by', 'comment_text', 'comment_date', 'likes_count'))

        df = pd.DataFrame(dfa)

        path = "Data/"+video_id+".csv"
        full_path = os.path.abspath(path)  # get the FULL path

        df.to_csv(path)
        return full_path

    except:
        return False
    


def get_video_id(url):
    u_pars = urlparse(url)
    quer_v = parse_qs(u_pars.query).get('v')
    if quer_v:
        return quer_v[0]
    pth = u_pars.path.split('/')
    if pth:
        return pth[-1]
  

def scrape_comments(url):
    #credentials
    api_key = os.getenv('GOOGLE_API_KEY')
    video_id = get_video_id(url)
    res = video_comments(video_id,api_key)
    return res