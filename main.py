import datetime as dt

from data_manager import DataManager
from playlist import Playlist
from dateutil.relativedelta import relativedelta
from pprint import PrettyPrinter

pp = PrettyPrinter(indent= 2)
 
search_year = int(input("Enter the year: \n"))
search_month = int(input("Enter the month: \n"))
search_day = int(input("Enter the day: \n"))

search_date = dt.datetime(
    year = search_year,
    month = search_month,
    day = search_day
)

search_date_string = search_date.strftime("%Y-%m-%d")

data = DataManager(date = search_date_string)

song_list = data.get_song_data()
artist_list = data.get_artist_data()

print(song_list)
print(artist_list)

with open("Song_list.txt", mode = "w") as file:
    for song in song_list:
        file.write(f"{song}\n")
        
with open("Music_artist.txt", mode = "w") as file2:
    for artist in artist_list:
        file2.write(f"{artist}\n")
        
sp = Playlist()

search_results_list = sp.search_results(
    song_list = song_list,
    date = search_date_string
    )

#extract the song URI for each song

def create_uri_list(search_results: dict, track_listing: list):
    uri_search_results = []
    song = {}
    missing_songs = []
    for _ in range(len(search_results_list)):
        try:
            uri = search_results[_]["tracks"]["items"][0]["uri"]
        
        except IndexError:
            print(f"The song: The song: {track_listing[_]} does not exist in Spotify.\nThis song will be skipped.")
            missing_songs.append(track_listing[_])
            continue
        
        else:
            song["title"] = track_listing[_]
            song["uri"] = uri
            uri_search_results.append(song)
            
    return uri_search_results, missing_songs

uri_list, missing_songs = create_uri_list(
    search_results= search_results_list,
    track_listing = song_list
)
        
new_date = search_date - relativedelta(years = 1)
new_date_string = new_date.strftime("%Y-%m-%d")

if len(missing_songs) > 0:
    missing_song_search_results = sp.search_results(
        song_list = missing_songs,
        date = new_date_string
        )
    
print(missing_song_search_results)

missing_song_uri_list, remaining_missing_songs = create_uri_list(
    search_results = missing_song_search_results,
    track_listing = song_list 
)



get_all_playlists = sp.get_user_playlists()

user_playlist_creation = input("Would you like to create a new playlist?\nType Yes or No")

user_playlist_creation = user_playlist_creation.capitalize()

if user_playlist_creation == "Yes":
    sp.create_playlist()

else:
    playlist_name = sp.playlist_name

for _ in range(len(get_all_playlists["items"])):
    if get_all_playlists["items"][_]["name"] == playlist_name:
        playlist_uri = get_all_playlists["items"][_]["uri"]

playlist_id = playlist_uri.split(":")[2]

sp.add_songs(
    playlist_id = playlist_id,
    tracks = uri_search_results
)
