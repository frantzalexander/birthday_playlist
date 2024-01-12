import requests

from spotipy import oauth2
from decouple import config

class Playlist:
    def __init__(self, song, artist):
        self.__client_id = config("CLIENT_ID")
        self.__client_key = config("CLIENT_SECRET")
        self.song = song
        self.artist = artist

       
    def create_playlist(self):
         self.response = oauth2.SpotifyClientCredentials(
             client_id = self.__client_id,
             client_key = self.__client_key,
         )
       
       