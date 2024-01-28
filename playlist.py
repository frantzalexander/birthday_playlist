import spotipy
from spotipy.oauth2 import SpotifyOAuth
from decouple import config

class Playlist:
    def __init__(self, song_list, artist_list, date):
        self.__client_id = config("CLIENT_ID")
        self.__client_key = config("CLIENT_SECRET")
        self.song_list = song_list
        self.artist_list = artist_list
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

    def search_song(self, song_track):
        self.song_track = song_track
        self.year_string = self.date[:4]
        self.year = int(self.year_string)
        results = self.sp.search(
            q = f"track:{self.song_track} year:{self.year}", 
            type= "track", 
            limit= 1
            )
        
        return results
    
    def search_results(self):
        self.search_list = [self.search_song(song) for song in self.song_list]
        
        return self.search_list
        
        
        
