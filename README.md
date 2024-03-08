# Project Overview
A program that creates a Spotify playlist containing the song titles from the [Billboard hot 100](https://www.billboard.com/charts/hot-100/) rankings website.


## Objectives
- Ask the user for a past date.
- Acquire the song title and artist name data utilizing webscraping.
- Perform search queries utilizing the Spotify API.
- Create a playlist.
- Add songs to the playlist.

## Results
![image](https://github.com/frantzalexander/birthday_playlist/assets/128331579/9bd70017-0e41-4a2e-a0a6-5dd7bdfc9d8e)


## Process
The project consists of 3 modules:
- Main Module
- Playlist Module
- Data Manager Module

The Main Module is responsible for executing the program.


The Playlist Module retrieves song data utilizing the Spotify API. 


It also performs the query that creates the user playlist and adds songs to the playlist. 


The Data Manager Module utilizes the Requests and Beautiful Soup Python Libraries to acquire the song information from webscraping the internet.


```mermaid
flowchart TD
start(((START)))
data_manager[]
