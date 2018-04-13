import datorama
import requests
import datetime

""" 
Youtube Public API Script

This script pulls data such as number of views, comments, subscribers, 
and videos from the YouTube Data API for a given list of accounts. Useful until
we have an official YouTube public API. This script can be deployed as a 
Python retrieval and scheduled to run on a daily basis. If you want to run 
it more frequently, be sure to alter the date to include a timestamp as well.
This will prevent multiple daily runs from overwriting each other. Finally,
you will need to supply this script with YouTube API key, visit 
https://developers.google.com/youtube/v3/getting-started to obtain yours.

""" 
# Add YouTube channel IDs that you would like to pull stats about to this list, you can obtain the ID
# for a given channel by usign the endpoint on this page to retrieve the channel by YouTube username:
# https://developers.google.com/youtube/v3/docs/channels/list (NB: you need an API key to use this)
accounts = [{"Name":"NASCAR", "YouTubeID":"UCuN9hYw2RpoAW8rZ3VK3isA"}, {"Name":"F1", "YouTubeID": "UCB_qr75-ydFVKSF9Dmo6izg"}, 
{"Name":"PGATOUR", "YouTubeID":"UCKwGZZMrhNYKzucCtTPY2Nw"}, {"Name":"MotoGP", "YouTubeID":"UC8pYaQzbBBXg9GIOHRvTmDQ"}, 
{"Name":"IndyCar", "YouTubeID":"UCy1F61QvUUQXAXi2Voa_fUw"}, {"Name":"ufc", "YouTubeID":"UCvgfXK4nTYKudb0rFR6noLA"}, 
{"Name":"WWE", "YouTubeID":"UC2Oxk5J24C1gYhDWpRDNPlw"}]

# Change the date format below to pull data more frequently than daily
date_granularity = "%d-%m-%Y"

# YouTube API credentials
api_base_url = 'https://www.googleapis.com/youtube/v3/'
part = 'snippet,statistics'
api_key = "AIzaSyDbDLo8KC-izu3WXgoG3PMmar__0oSA4lE"
endpoint = "channels"
params = {'key': api_key, 'part': part}

# Generating a list of values for our header row 
headers = 'Date,Account,Views,Comments,Subscribers,Videos'
data = ''
now = datetime.datetime.now()
date = now.strftime(date_granularity)

# Iterate through accounts and request stats from YouTube API
for account in accounts:
	params["id"] = account["YouTubeID"]
	response = requests.get(api_base_url+endpoint, params=params).json()
	id = response["items"][0]["id"]
	statistics = response["items"][0]["statistics"]
	data += '\n'
	data += date + ','
	data += id + ','
	data += str(statistics["viewCount"]) + ','
	data += str(statistics["commentCount"]) + ','
	data += str(statistics["subscriberCount"]) + ','
	data += str(statistics["videoCount"])

if len(data) > 0: 
	# Add CSV headers to data
	csv = headers + data
	# Saving the csv file, based on the input string 
	datorama.save_csv(csv)
	print(csv)
