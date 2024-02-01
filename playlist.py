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
        self.scope = "playlist-modify-public"
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
        self.playlist_name = ""
        
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
        
    def create_playlist(self):
        self.playlist_name = f"Billboard Hot 100 songs on {self.date}"
        self.playlist_description = "Top Songs"
        
        self.sp.user_playlist_create(
            user = self.user_id,
            name = self.playlist_name,
            public = True,
            description= self.playlist_description
        )
        
    def get_user_playlists(self):
        self.all_user_playlists = self.sp.user_playlists(
            user = self.user_id
        )
        
        return self.all_user_playlists

    def make_playlist(self):
        self.create_playlist()
        
    def add_songs(self, playlist_id: str, tracks: list):
        self.playlist_id = playlist_id
        self.tracks = tracks
        self.sp.user_playlist_add_tracks(
            user = self.user_id,
            playlist_id = self.playlist_id,
            tracks = self.tracks
        )
    