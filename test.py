# import some Python dependencies
# python 2
# import urllib2

#python 3

import urllib3
import json
import datetime
import csv
import time

app_id = ""
app_secret = ""
access_token = app_id + "|" + app_secret

page_id = 'nytimes'


def testFacebookPageData(page_id, access_token):
    # construct the URL string
    base = "https://graph.facebook.com/v2.11"
    node = "/" + page_id
    parameters = "/?access_token=%s" % access_token
    url = base + node + parameters

    # retrieve data
    req = urllib3.Request(url)
    response = urllib3.urlopen(req)
    data = json.loads(response.read())

    print(json.dumps(data, indent=4, sort_keys=True))


testFacebookPageData(page_id, access_token)