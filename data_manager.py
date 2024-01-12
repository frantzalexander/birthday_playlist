import requests

from typing import List
from bs4 import BeautifulSoup

class DataManager:
    
    def __init__(self, date):
        self.website_url = "https://www.billboard.com/charts/hot-100/"
        self.date = date
        
    def extract_text(self, data):
        """Function to extract & clean text data."""
        self.data = data
        self.text_data = self.data.getText().strip()
        self.clean_data = self.text_data.lstrip("-")
        return self.clean_data
    
    def get_song_data(self)-> list[str]:
        """
        Function to parse website and outputs a list containing website element text
        """
        self.search_website = self.website_url + self.date
        self.response = requests.get(self.search_website)
        self.response.raise_for_status()
        self.website_data = self.response.text
        self.soup = BeautifulSoup(self.website_data, "html.parser")
        
        self.songs_tags = self.soup.select(
            selector = "li ul li h3"
        )

        self.songs = [self.extract_text(song) for song in self.songs_tags]
        
        return self.songs
        
    def get_artist_data(self) -> list[str]:
        """
        Function to parse website and outputs a list containing website element text
        """
        self.search_website = self.website_url + self.date
        self.response = requests.get(self.search_website)
        self.response.raise_for_status()
        self.website_data = self.response.text
        self.soup = BeautifulSoup(self.website_data, "html.parser")
        
        self.artist_tags = self.soup.select(
            selector = "li ul li span"
        )
        
        self.artists_list = [self.extract_text(artist) for artist in self.artist_tags]

        self.artists = []
        for artist in self.artists_list:
            if not artist.isdigit() and artist != "":
                self.artists.append(artist)
                
        return self.artists
            
            