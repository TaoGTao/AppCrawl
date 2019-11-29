from mitmproxy import ctx, http
import json
from pymongo import MongoClient
import re

def response(flow):
    client = MongoClient('127.0.0.1:27017')
    coll = client['app短视频']['小红书']
    url = 'https://www.xiaohongshu.com/api/sns/v9/search/notes?keyword'
    if flow.request.url.startswith(url):
        info = json.loads(flow.response.text)
        for inf in info['data']['notes']:
            # print(inf)
            # for di in inf['data']['notes']:
            coll.insert(inf)
        # client.close()
                # ctx.log(di)


#
# addons = [
#     RedBook()
# ]
