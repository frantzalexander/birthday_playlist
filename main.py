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

hot_100_song_list = data.get_song_data()
hot_100_artist_list = data.get_artist_data()

sp = Playlist()

hot_100_search_results = sp.search_results(
    song_list = hot_100_song_list,
    date = search_date_string
    )

#extract the song URI for each song
def create_uri_list(results: list, songtrack_list: list):
    uri_search_results = []
    missing_songs = []
    for _ in range(len(results)):
        try:
            uri = results[_]["tracks"]["items"][0]["uri"]
        
        except IndexError:
            missing_songs.append(songtrack_list[_])
            continue
        
        else:
            song_list = {}
            song_list["title"] = songtrack_list[_]
            song_list["uri"] = uri
            uri_search_results.append(song_list)
               
    return uri_search_results, missing_songs

song_uri_list, missing_song_list = create_uri_list(
    results= hot_100_search_results,
    songtrack_list = hot_100_song_list
)

#search for missing songs released 1 year earlier
new_date = search_date - relativedelta(years = 1)
new_date_string = new_date.strftime("%Y-%m-%d")

missing_songs_search_results = sp.search_results(
    song_list = missing_song_list,
    date = new_date_string
    )
    
pp.pprint(missing_songs_search_results)

missing_song_uri_list, remaining_missing_songs = create_uri_list(
    results = missing_songs_search_results,
    songtrack_list = missing_song_list 
)
#search for the remaining songs by artist
def search_missing_song_artist(full_song_list: list, missing_song_list: list, full_artist_list: list):
    song_list = []
    
    for song in missing_song_list:
        missing_song_dict = {}
        song_index = full_song_list.index(song)
        song_artist = full_artist_list[song_index]
        missing_song_dict["song"] = song
        missing_song_dict["artist"] = song_artist
        song_list.append(missing_song_dict)
        
    return song_list

missing_song_and_artist_list = search_missing_song_artist(
    full_song_list = hot_100_song_list,
    missing_song_list = remaining_missing_songs,
    full_artist_list = hot_100_artist_list
)

missing_songs_search_by_artist_results = []

for item in missing_song_and_artist_list:
    missing_song = item["song"]
    missing_song_artist = item["artist"]
    search_result_missing_song = sp.search_song_by_artist(
        song_track = missing_song,
        artist = missing_song_artist
        )
    missing_songs_search_by_artist_results.append(search_result_missing_song)

song_list_by_artist, missing_songs_final = create_uri_list(
    results = missing_songs_search_by_artist_results,
    songtrack_list = remaining_missing_songs
) 

#create a list of available songs
full_song_list = []
full_song_list.extend(song_uri_list)
full_song_list.extend(missing_song_uri_list)
full_song_list.extend(song_list_by_artist)

#create a list of the song uri 
full_song_uri_list = [song["uri"] for song in full_song_list]

# Create playlist
sp.create_playlist()

get_all_playlists = sp.get_user_playlists()

playlist_name = sp.playlist_name

playlists_full_list = []
for playlist in get_all_playlists["items"]:
    playlists_full_list.append(playlist)
    
for playlist in playlists_full_list:
    if playlist["name"] == playlist_name:
        playlist_uri = playlist["uri"]

playlist_id = playlist_uri.split(":")[2]

sp.add_songs(
    playlist_id = playlist_id,
    tracks = full_song_uri_list
)
