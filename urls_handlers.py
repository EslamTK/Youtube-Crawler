import re

class UrlHandler(object):
    '''
    Abstract class that will handle the youtube url patterns and get the videos ids from the youtube api, 
    Subclass should be created for each pattern
    '''

    def __init__(self, api_requests_handler):
        self.api_requests_handler = api_requests_handler

    def get_playlist_id(self, url):
        raise NotImplementedError()
    
    def _get_uploads_playlist_id(self, channel_id=None, username=None):
        return self.api_requests_handler.\
        get_uploads_playlist_id(channel_id=channel_id, username=username)
    
    def save_videos_info(self, playlist_id):
        return self.api_requests_handler.\
        save_videos_info(playlist_id=playlist_id)

class ChannelUrlHandler(UrlHandler):

    def get_playlist_id(self, url):
        pattern = re.search(r'(?<=channel/)((\w)|\-)+', url)
        channel_id = pattern.group(0)

        return self._get_uploads_playlist_id(channel_id=channel_id)

class UserUrlHandler(UrlHandler):

    def get_playlist_id(self, url):
        pattern = re.search(r'(?<=user/)((\w)|\-)+', url)
        username = pattern.group(0)
        
        return self._get_uploads_playlist_id(username=username)

class PlaylistUrlHandler(UrlHandler):

    def get_playlist_id(self, url):
        pattern = re.search(r'(?<=list=)([\w\-])+', url)
        playlist_id = pattern.group(0)
        
        return playlist_id
