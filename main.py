import datetime as dt

from data_manager import DataManager
from playlist import Playlist
from dateutil.relativedelta import relativedelta

from pprint import PrettyPrinter

pp = PrettyPrinter(indent= 2)
 
search_year = int(input("Enter the year: \n"))
search_month = int(input("Enter the month: \n"))
search_day = int(input("Enter the day: \n"))

search = dt.datetime(
    year = search_year,
    month = search_month,
    day = search_day
)

search_date = search.strftime("%Y-%m-%d")

data = DataManager(date = search_date)

song_list = data.get_song_data()
artist_list = data.get_artist_data()

print(song_list)
print(artist_list)

# with open("Song_list.txt", mode = "w") as file:
#     for song in song_list:
#         file.write(f"{song}\n")
        
# with open("Music_artist.txt", mode = "w") as file2:
#     for artist in artist_list:
#         file2.write(f"{artist}\n")
        
sp = Playlist(
    song_list = song_list, 
    artist_list = artist_list,
    date = search_date
    )

search_results_list = sp.search_results()

# pp.pprint(search_results_list[0])

#extract the song URI for each song

uri_search_results = []

for _ in range(len(search_results_list)):
    try:
        uri = search_results_list[_]["tracks"]["items"][0]["uri"]
    
    except KeyError:
        continue
    
    else:
        uri_search_results.append(uri)
    

