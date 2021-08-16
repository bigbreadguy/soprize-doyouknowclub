import os
import json

from html.parser import HTMLParser

from apiclient.discovery import build
from apiclient.errors import HttpError
from oauth2client.tools import argparser

def youtube_search(options):
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
        developerKey=DEVELOPER_KEY)

    # Call the search.list method to retrieve results matching the specified
    # query term.
    search_response = youtube.search().list(
        publishedAfter=options.published_after,
        q=options.q,
        type=options.type,
        part="id,snippet",
        maxResults=options.max_results
    ).execute()

    search_res_dict = dict()

    # Add each result to the appropriate list, and then display the lists of
    # matching videos, channels, and playlists.
    for search_result in search_response.get("items", []):
        if search_result["id"]["kind"] == "youtube#video":
            search_res_dict[search_result["snippet"]["title"]] = search_result["id"]["videoId"]

    return search_res_dict

def youtube_video(options):
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
        developerKey=DEVELOPER_KEY)

    # Call the search.list method to retrieve results matching the specified
    # query term.
    search_response = youtube.videos().list(
        part="snippet,player",
        id=options.id
    ).execute()

    search_res_dict = dict()

    # Add each result to the appropriate list, and then display the lists of
    # matching videos, channels, and playlists.
    for search_result in search_response.get("items", []):
        search_res_dict[search_result["snippet"]["title"]] = str(search_result["player"]["embedHtml"])

    return search_res_dict

class URLParser(HTMLParser):
    def __init__(self):
        super(URLParser, self).__init__()
        self.src = ""

    def handle_starttag(self, tag, attrs):
        for attr in attrs:
            if attr[0] == "src":
                self.src = "https:" + attr[1]