import requests

import spotipy
from spotipy.oauth2 import SpotifyOAuth
from decouple import config

class Playlist:
    def __init__(self, song, artist, date):
        self.__client_id = config("CLIENT_ID")
        self.__client_key = config("CLIENT_SECRET")
        self.song = song
        self.artist = artist
        self.date = date
        self.scope = "playlist-modify-private"
        self.uri = "http://example.com"
        self.sp = spotipy.Spotify(
            auth_manager= SpotifyOAuth(
                scope = self.scope,
                client_id = self.__client_id,
                client_secret = self.__client_key,
                redirect_uri = self.uri,
                username= "Pyrial",
                show_dialog = True,
                cache_path= "token.txt"
                )
            )
        
        self.user_id = self.sp.current_user()["id"]
       
    def search_song(self):
        results = self.sp.search(
            q= self.song[0], 
            type= "track", 
            limit= 1
            )
        
        return results
        
        
        
