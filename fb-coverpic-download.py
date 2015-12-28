#Author Aditya Mehra
# Python module for connecting fb with graph API and downloading user's cover picture 
#in local filesystem


# Downloading the needed modules
import urllib2  
import json




def fb_data(page_id_uname,token):
    api_endpoint = "https://graph.facebook.com/v2.4/"
    graph_url = api_endpoint+page_id_uname+"?fields=cover&access_token="+token
    try:
        api_request = urllib2.Request(graph_url)
        api_response = urllib2.urlopen(api_request)
        
        try:
            return json.loads(api_response.read())
        except (ValueError, KeyError, TypeError):
            return "JSON error"

    except IOError, error:
        if hasattr(error, 'code'):
            return error.code
        elif hasattr(error, 'reason'):
            return error.reason

page_id_uname = "#####" # provide your username or id
#You can get id by accessing your fb page and copying the numbers after id=######

token = "######"  #provide the  Access Token
# please visit page https://developers.facebook.com/tools/explorer for getting the access token
        
page_data = fb_data(page_id_uname,token)
print "page_data",page_data

# code for fetching the URL for cover picture and downloading cover picture to the local filesystem
cover_url =  page_data['cover']['source']
img = urllib2.urlopen(cover_url)
local_path = "####" #For e.g :: /root/data
localFile = open(local_path, 'wb')
localFile.write(img.read())
localFile.close()
print "done"
